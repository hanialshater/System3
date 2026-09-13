import {normalizeArtEdit,hasArtEdits} from './art-state.js';
const images=new Map();
export function loadArtImage(src){
 if(src.startsWith('data:'))return new Promise((resolve,reject)=>{const img=new Image();img.onload=()=>resolve(img);img.onerror=()=>reject(new Error('Could not preview the edited illustration.'));img.src=src;});
 if(!images.has(src))images.set(src,new Promise((resolve,reject)=>{const img=new Image();img.crossOrigin='anonymous';img.onload=()=>resolve(img);img.onerror=()=>{images.delete(src);reject(new Error('The illustration could not be loaded. Your original is unchanged.'));};img.src=src;}));
 return images.get(src);
}
export async function renderArt(src,value,{maxPixels=1800,force=false}={}){
 const e=normalizeArtEdit(value);if(!force&&!hasArtEdits(e))return src;
 const img=await loadArtImage(src),c=e.crop;
 const sw=img.naturalWidth*c.width,sh=img.naturalHeight*c.height;
 const factor=Math.min(1,maxPixels/Math.max(sw,sh));const w=Math.max(1,Math.round(sw*factor)),h=Math.max(1,Math.round(sh*factor));
 const angle=e.rotation*Math.PI/180;
 const canvas=document.createElement('canvas');canvas.width=Math.max(1,Math.ceil(Math.abs(w*Math.cos(angle))+Math.abs(h*Math.sin(angle))));canvas.height=Math.max(1,Math.ceil(Math.abs(w*Math.sin(angle))+Math.abs(h*Math.cos(angle))));
 const ctx=canvas.getContext('2d');ctx.translate(canvas.width/2,canvas.height/2);ctx.rotate(angle);ctx.scale(e.flipX?-1:1,e.flipY?-1:1);
 ctx.globalAlpha=e.opacity;ctx.filter=`brightness(${1+e.brightness}) contrast(${1+e.contrast}) saturate(${e.saturation})`;
 ctx.drawImage(img,img.naturalWidth*c.x,img.naturalHeight*c.y,sw,sh,-w/2,-h/2,w,h);
 return canvas.toDataURL('image/png');
}
