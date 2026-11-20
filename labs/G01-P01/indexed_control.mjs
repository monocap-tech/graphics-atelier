// Original isolated control; run with node indexed_control.mjs.
function runControl(){
  const w=16,h=16,indices=[];
  // Original procedural fixture: an asymmetric mechanical silhouette, not copied art.
  for(let y=0;y<h;y++) for(let x=0;x<w;x++){
    let k=0;
    if(y>=3&&y<=12&&Math.abs(x-7.5)<=((y<7)?y-2:5.5)) k=1;
    if(k&&y>=5&&y<=10&&x>=5&&x<=10) k=2;
    if(k&&y>=6&&y<=7&&x>=7&&x<=8) k=3;
    if(y>=9&&y<=11&&x===13) k=4;
    if(y>=12&&y<=13&&(x===5||x===10)) k=4;
    indices.push(k);
  }
  const a=[[0,0,0,0],[34,39,55,255],[68,124,151,255],[179,228,238,255],[246,179,71,255]];
  const b=[[0,0,0,0],[45,26,49,255],[155,67,114,255],[238,167,204,255],[114,229,167,255]];
  const order=[0,3,1,4,2]; // new index -> old index
  const permuted=order.map(i=>a[i]);
  const mapped=indices.map(i=>order.indexOf(i));
  const render=(data,p)=>data.flatMap(i=>p[i]);
  const identical=(a,b)=>a.length===b.length&&a.every((v,i)=>v===b[i]);
  const alpha=rgba=>rgba.filter((_,i)=>i%4===3);
  const base=render(indices,a),recolor=render(indices,b),wrong=render(indices,permuted),right=render(mapped,permuted);
  const counts=a.map((_,i)=>indices.filter(x=>x===i).length);
  const changed=(a,b)=>a.filter((_,i)=>i%4===0&&!identical(a.slice(i,i+4),b.slice(i,i+4))).length;
  const check={
    fixed_cell:indices.length===w*h,
    all_roles_used:counts.every(n=>n>0),
    alpha_equal_recolor:identical(alpha(base),alpha(recolor)),
    recolor_changes_visible_pixels:changed(base,recolor)===w*h-counts[0],
    palette_reorder_without_remap_changes_image:!identical(base,wrong),
    reorder_with_remap_preserves_rgba:identical(base,right),
    remap_preserves_transparent_index:indices.every((x,i)=>(x===0)===(mapped[i]===0))
  };
  if(!Object.values(check).every(Boolean))throw Error(JSON.stringify(check));
  return {width:w,height:h,counts,visible_pixels:w*h-counts[0],recolor_changed_pixels:changed(base,recolor),unremapped_reorder_changed_pixels:changed(base,wrong),remapped_reorder_changed_pixels:changed(base,right),check};
}
console.log(JSON.stringify(runControl(), null, 2));
