import argparse,json,hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright
parser=argparse.ArgumentParser()
parser.add_argument('--study-dir',type=Path,default=Path(__file__).resolve().parent.parent/'G06-P07')
parser.add_argument('--output',type=Path,default=Path('mutation-results.json'))
parser.add_argument('--chromium',default='/usr/bin/chromium')
a=parser.parse_args()
src=(a.study_dir/'preview.html').read_text()
harness=(a.study_dir/'check.py').read_text()
check=harness.split("results=page.evaluate('''",1)[1].split("''')",1)[0]
mutations={
'baseline':[],
'blank_abstract':[("s==='abstract'?abstract(t,fx):interactive(s,t,fx)","s==='abstract'?{phase:'autonomous',active:false}:interactive(s,t,fx)")],
'decoration_toggle_inert':[("const f=s==='abstract'?abstract(t,fx):interactive(s,t,fx)","const f=s==='abstract'?abstract(t,false):interactive(s,t,false)")],
'flight_core_only_at_probed_ticks':[("poly([[f.x+3,45],[f.x-6,42],[f.x-4,45],[f.x-6,48]],ivory)","if(t===12||t===27)poly([[f.x+3,45],[f.x-6,42],[f.x-4,45],[f.x-6,48]],ivory)")],
'impact_persists_until_end':[("if(a<5){line(96,40,96,50,ivory,3,1-a/5);dot(96,45,gold,2)}","if(a<72){line(96,40,96,50,ivory,3,1);dot(96,45,gold,2)}")],
'moving_guard_stationary':[("s==='moving'?15+Math.min(t,30):45","s==='moving'?45:45")],
'phantom_core_after_cancellation':[("if(f.phase==='cancelled'&&fx&&t-f.event<10)","if(f.phase==='cancelled'&&t>=19)poly([[f.x+3,45],[f.x-6,42],[f.x-4,45],[f.x-6,48]],ivory);if(f.phase==='cancelled'&&fx&&t-f.event<10)")],
'positive_control_remove_all_cores':[("poly([[f.x+3,45],[f.x-6,42],[f.x-4,45],[f.x-6,48]],ivory)","void 0")],
'positive_control_disable_hit':[("Math.abs(45-gy)<=9","false")],
}
rows=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path=a.chromium,args=['--no-sandbox']); version=b.version
 for name,edits in mutations.items():
  s=src
  for old,z in edits:
   assert s.count(old)==1,(name,s.count(old));s=s.replace(old,z,1)
  page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.set_content(s);r=page.evaluate(check);page.close()
  rows.append({'name':name,'edits':edits,'failed_checks':[k for k,v in r['checks'].items() if not v],'survived':all(r['checks'].values()) and not errors,'page_errors':errors})
 b.close()
out={'browser':version,'source_sha256':hashlib.sha256(src.encode()).hexdigest(),'harness_sha256':hashlib.sha256(harness.encode()).hexdigest(),'rows':rows};a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
