const clamp=(v,min,max,fallback)=>typeof v==='number'&&Number.isFinite(v)?Math.max(min,Math.min(max,v)):fallback;
export function normalizeArtEdit(value={}) {
 const e=value&&typeof value==='object'?value:{};const c=e.crop||{};
 const x=clamp(c.x,0,.95,0),y=clamp(c.y,0,.95,0);
 return {version:1,crop:{x,y,width:clamp(c.width,.05,1-x,1-x),height:clamp(c.height,.05,1-y,1-y)},rotation:clamp(e.rotation,-180,180,0),flipX:e.flipX===true,flipY:e.flipY===true,brightness:clamp(e.brightness,-.5,.5,0),contrast:clamp(e.contrast,-.5,.5,0),saturation:clamp(e.saturation,0,2,1),opacity:clamp(e.opacity,.1,1,1)};
}
export function hasArtEdits(value){return JSON.stringify(normalizeArtEdit(value))!==JSON.stringify(normalizeArtEdit());}
