// Original analytic control, independent of any commercial renderer.
function projectionControl(){
 const w=640,h=360,fy=h/(2*Math.tan(Math.PI/6)),R=10;
 const points=[[320,180],[160,90],[480,90],[160,270],[480,270]];
 const plus=(a,b)=>a.map((v,i)=>v+b[i]),sub=(a,b)=>a.map((v,i)=>v-b[i]),mul=(a,s)=>a.map(v=>v*s),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
 function basis(deg){const a=deg*Math.PI/180;return {p:[R*Math.sin(a),0,-R*Math.cos(a)],r:[Math.cos(a),0,Math.sin(a)],u:[0,1,0],f:[-Math.sin(a),0,Math.cos(a)]};}
 function ray(c,s){return plus(c.f,plus(mul(c.r,(s[0]-w/2)/fy),mul(c.u,(h/2-s[1])/fy)));}
 function project(c,p){const d=sub(p,c.p),z=dot(d,c.f);if(z<=1e-9)return null;return [w/2+fy*dot(d,c.r)/z,h/2-fy*dot(d,c.u)/z];}
 function err(a,b){return a?Math.hypot(a[0]-b[0],a[1]-b[1]):null;}
 const base=basis(0),fixed=points.map(s=>plus(base.p,mul(ray(base,s),R)));
 const rows=[0,15,30,45,60,75,90].map(deg=>{
  const c=basis(deg);let invalid=0,maxFixed=0,planeValid=0,maxPlaneError=0,maxDepthError=0,maxPlaneDistance=0;
  for(let i=0;i<points.length;i++){
   const s=points[i],d=ray(c,s),depthPoint=plus(c.p,mul(d,R));
   maxDepthError=Math.max(maxDepthError,err(project(c,depthPoint),s));
   const e=err(project(c,fixed[i]),s);if(e===null)invalid++;else maxFixed=Math.max(maxFixed,e);
   if(Math.abs(d[2])>1e-9){const t=-c.p[2]/d[2];if(t>1e-9){const p=plus(c.p,mul(d,t));planeValid++;maxPlaneError=Math.max(maxPlaneError,err(project(c,p),s));maxPlaneDistance=Math.max(maxPlaneDistance,t);}}
  }
  const round=x=>Number(x.toFixed(9));
  return {yaw_deg:deg,anchored_max_error_px:round(maxFixed),anchored_behind:invalid,camera_depth_max_error_px:round(maxDepthError),plane_valid:planeValid,plane_max_error_px:planeValid?round(maxPlaneError):null,plane_max_forward_depth:planeValid?round(maxPlaneDistance):null};
 });
 const checks={baseline_fixed_matches:rows[0].anchored_max_error_px<1e-8,depth_roundtrip:rows.every(r=>r.camera_depth_max_error_px<1e-8),valid_plane_roundtrip:rows.every(r=>r.plane_max_error_px===null||r.plane_max_error_px<1e-8),fixed_drifts:rows.some(r=>r.anchored_max_error_px>1),plane_fails:rows.some(r=>r.plane_valid<points.length)};
 if(!Object.values(checks).every(Boolean)) throw Error(JSON.stringify({rows,checks}));
 return {viewport:[w,h],vertical_fov_deg:60,depth:R,points,rows,checks};
}
console.log(JSON.stringify(projectionControl(),null,2));
