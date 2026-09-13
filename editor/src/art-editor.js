import Konva from 'konva';
import {normalizeArtEdit} from './art-state.js';
import {loadArtImage,renderArt} from './art-render.js';
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export async function openArtEditor(figure,onApply){
 let edit=normalizeArtEdit(figure.edit),height=figure.height,mode='transform',undo=[],redo=[],closed=false,revision=0,cropRect=null,imageBox=null,renderScale=1;
 const startingHeight=height;
 const dialog=document.createElement('dialog');dialog.className='art-dialog';dialog.setAttribute('aria-label','Edit artwork');
 dialog.innerHTML=`<header class="art-header"><div><span class="art-eyebrow">ARTWORK STUDIO</span><h2>${escape(figure.title)}</h2></div><div class="art-history"><button data-tool="undo" aria-label="Undo artwork edit">↶</button><button data-tool="redo" aria-label="Redo artwork edit">↷</button></div><button data-tool="cancel" class="art-close" aria-label="Cancel artwork editing">×</button></header><div class="art-workspace"><div class="art-canvas-pane"><div class="art-tools"><button class="selected" data-mode="transform">Transform</button><button data-mode="crop">Crop</button><button data-tool="flip-x">Flip horizontal</button><button data-tool="flip-y">Flip vertical</button></div><div class="art-stage-wrap"><div id="art-stage"></div><p class="art-loading">Loading illustration…</p></div><div class="art-canvas-caption"><span id="art-mode-hint">Drag the corner handles to resize. Use the top handle to rotate.</span><span>Konva canvas</span></div></div><aside class="art-adjustments"><h3>ADJUSTMENTS</h3><label>Rotation <output data-output="rotation">0°</output><input data-adjust="rotation" type="range" min="-180" max="180" step="1"></label><label>Page height <output data-output="height"></output><input data-adjust="height" type="range" min="30" max="110" step="1"></label><hr><label>Brightness <output data-output="brightness"></output><input data-adjust="brightness" type="range" min="-.5" max=".5" step=".01"></label><label>Contrast <output data-output="contrast"></output><input data-adjust="contrast" type="range" min="-.5" max=".5" step=".01"></label><label>Saturation <output data-output="saturation"></output><input data-adjust="saturation" type="range" min="0" max="2" step=".01"></label><label>Opacity <output data-output="opacity"></output><input data-adjust="opacity" type="range" min=".1" max="1" step=".01"></label><button data-tool="grayscale" class="art-quiet">Black & white</button><button data-tool="reset" class="art-quiet">Reset to original</button><p class="art-note">Your original stays intact. Crop, color and transform settings save with the chapter.</p></aside></div><footer class="art-footer"><span id="art-status" role="status">Changes apply to this illustration only.</span><button data-tool="cancel" class="art-quiet">Cancel</button><button data-tool="apply" class="art-apply" disabled>Apply to page</button></footer>`;
 document.body.append(dialog);dialog.showModal();
 const $=s=>dialog.querySelector(s);const stageHost=$('#art-stage');const wrap=$('.art-stage-wrap');
 const stage=new Konva.Stage({container:stageHost,width:Math.max(240,wrap.clientWidth),height:Math.max(250,wrap.clientHeight)});
 const layer=new Konva.Layer();stage.add(layer);let node=null,transformer=null;
 const state=()=>JSON.stringify({edit,height});
 function checkpoint(){undo.push(state());if(undo.length>50)undo.shift();redo=[];}
 function controls(){
  dialog.querySelectorAll('[data-adjust]').forEach(el=>{const k=el.dataset.adjust,v=k==='height'?height:edit[k];el.value=v;$(`[data-output="${k}"]`).textContent=k==='rotation'?`${Math.round(v)}°`:k==='height'?`${Math.round(v)} mm`:`${Math.round((['brightness','contrast'].includes(k)?v:v-1)*100)}${['brightness','contrast','saturation'].includes(k)?'%':''}`;if(k==='opacity')$('[data-output="opacity"]').textContent=`${Math.round(v*100)}%`;});
  $('[data-tool="undo"]').disabled=!undo.length;$('[data-tool="redo"]').disabled=!redo.length;
  dialog.querySelectorAll('[data-mode]').forEach(b=>b.classList.toggle('selected',b.dataset.mode===mode));
  $('#art-mode-hint').textContent=mode==='crop'?'Move and resize the crop rectangle. Switch to Transform to see the result.':'Drag corner handles to resize on the page. Use the top handle to rotate.';
  dialog.querySelectorAll('[data-adjust]').forEach(el=>el.disabled=mode==='crop');
 }
 function commitCrop(){
  if(mode!=='crop'||!cropRect||!imageBox)return;
  edit.crop={x:(cropRect.x()-imageBox.x)/imageBox.w,y:(cropRect.y()-imageBox.y)/imageBox.h,width:cropRect.width()*cropRect.scaleX()/imageBox.w,height:cropRect.height()*cropRect.scaleY()/imageBox.h};edit=normalizeArtEdit(edit);
 }
 async function draw(){
  const id=++revision;controls();
  try{
   const source=mode==='crop'?figure.art:await renderArt(figure.art,{...edit,rotation:0},{maxPixels:1200,force:true});
   const img=await loadArtImage(source);if(closed||id!==revision)return;
   layer.destroyChildren();const W=stage.width(),H=stage.height();
   const factor=Math.min((W-90)/img.naturalWidth,(H-90)/img.naturalHeight);
   if(mode==='crop'){
    const w=img.naturalWidth*factor,h=img.naturalHeight*factor,x=(W-w)/2,y=(H-h)/2;imageBox={x,y,w,h};
    node=new Konva.Image({image:img,x,y,width:w,height:h,opacity:.75,listening:false});layer.add(node);
    cropRect=new Konva.Rect({x:x+edit.crop.x*w,y:y+edit.crop.y*h,width:edit.crop.width*w,height:edit.crop.height*h,stroke:'#93c9e6',strokeWidth:2,draggable:true,fill:'rgba(255,255,255,.07)',dragBoundFunc:pos=>({x:Math.min(x+w-cropRect.width()*cropRect.scaleX(),Math.max(x,pos.x)),y:Math.min(y+h-cropRect.height()*cropRect.scaleY(),Math.max(y,pos.y))})});layer.add(cropRect);
    transformer=new Konva.Transformer({nodes:[cropRect],rotateEnabled:false,keepRatio:false,flipEnabled:false,borderStroke:'#93c9e6',anchorFill:'#fff',anchorStroke:'#32657b',anchorSize:9,boundBoxFunc:(old,next)=>next.width<20||next.height<20||next.x<x-2||next.y<y-2||next.x+next.width>x+w+2||next.y+next.height>y+h+2?old:next});layer.add(transformer);
    cropRect.on('dragstart transformstart',checkpoint);cropRect.on('dragend transformend',()=>{commitCrop();controls();});
   }else{
    const a=edit.rotation*Math.PI/180,rw=Math.abs(img.naturalWidth*Math.cos(a))+Math.abs(img.naturalHeight*Math.sin(a)),rh=Math.abs(img.naturalWidth*Math.sin(a))+Math.abs(img.naturalHeight*Math.cos(a));
    renderScale=Math.min((W-90)/rw,(H-90)/rh)*Math.max(.35,Math.min(1,.8*height/startingHeight));
    node=new Konva.Image({image:img,x:W/2,y:H/2,offsetX:img.naturalWidth/2,offsetY:img.naturalHeight/2,width:img.naturalWidth,height:img.naturalHeight,scaleX:renderScale,scaleY:renderScale,rotation:edit.rotation});layer.add(node);
    transformer=new Konva.Transformer({nodes:[node],keepRatio:true,flipEnabled:false,enabledAnchors:['top-left','top-right','bottom-left','bottom-right'],borderStroke:'#93c9e6',anchorFill:'#fff',anchorStroke:'#32657b',anchorSize:9,rotateAnchorOffset:27,boundBoxFunc:(old,next)=>Math.abs(next.width)<35||Math.abs(next.height)<35?old:next});layer.add(transformer);
    node.on('transformstart',checkpoint);node.on('transformend',()=>{height=Math.max(30,Math.min(110,height*Math.abs(node.scaleY())/renderScale));edit.rotation=((node.rotation()+540)%360)-180;draw();});
   }
   layer.draw();$('.art-loading').hidden=true;$('[data-tool="apply"]').disabled=false;
  }catch(e){$('#art-status').textContent=e.message;$('.art-loading').textContent='Illustration unavailable';$('[data-tool="apply"]').disabled=true;}
 }
 function close(){if(closed)return;closed=true;revision++;observer.disconnect();stage.destroy();dialog.close();dialog.remove();}
 async function action(tool){
  if(tool==='cancel'){close();return;}
  if(tool==='apply'){commitCrop();onApply({edit:normalizeArtEdit(edit),height:Math.round(height)});close();return;}
  if(tool==='undo'||tool==='redo'){
   const source=tool==='undo'?undo:redo,target=tool==='undo'?redo:undo;if(!source.length)return;target.push(state());const saved=JSON.parse(source.pop());edit=saved.edit;height=saved.height;await draw();return;
  }
  commitCrop();checkpoint();mode='transform';
  if(tool==='flip-x')edit.flipX=!edit.flipX;if(tool==='flip-y')edit.flipY=!edit.flipY;
  if(tool==='grayscale')edit.saturation=0;if(tool==='reset'){edit=normalizeArtEdit();height=startingHeight;}
  await draw();
 }
 dialog.querySelectorAll('[data-tool]').forEach(el=>el.onclick=()=>action(el.dataset.tool));
 dialog.querySelectorAll('[data-mode]').forEach(el=>el.onclick=()=>{if(mode===el.dataset.mode)return;commitCrop();mode=el.dataset.mode;draw();});
 dialog.querySelectorAll('[data-adjust]').forEach(el=>{
  let dragging=false;el.addEventListener('input',()=>{if(!dragging){checkpoint();dragging=true;}const k=el.dataset.adjust;if(k==='height')height=+el.value;else edit[k]=+el.value;draw();});
  el.addEventListener('change',()=>{dragging=false;});
 });
 dialog.addEventListener('cancel',e=>{e.preventDefault();close();});
 const observer=new ResizeObserver(()=>{if(closed)return;stage.size({width:Math.max(240,wrap.clientWidth),height:Math.max(250,wrap.clientHeight)});draw();});observer.observe(wrap);
 await draw();
}
