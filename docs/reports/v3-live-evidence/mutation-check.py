"""Run reviewed temporary-tool mutation probes through native isolation only."""
import json,sys
from dataclasses import asdict
from pathlib import Path
root=Path(r'D:\AI\AgentiX_v3');sys.path.insert(0,str(root/'src'))
from agentix.sandbox import WindowsSandbox
folder=root/'docs/reports/v3-live-evidence';name='warehouse_box_shipping_calculator'
code=(folder/f'{name}_code.py').read_bytes();tests=(folder/f'{name}_tests.py').read_bytes()
probes={
 'omit_shipping':(b'total_cost = preparation_cost + 5.00',b'total_cost = preparation_cost + 0.00'),
 'wrong_second_tier_rate':(b'* 1.50',b'* 1.00'),
 'accept_boolean':(b' or isinstance(number_of_boxes, bool)',b''),
}
results={}
for label,(old,new) in probes.items():
 assert old in code, label
 result=WindowsSandbox().execute(code.replace(old,new),tests,name,'',{})
 results[label]=asdict(result)
 (folder/'mutation-results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
 assert result.isolated and result.exit_code!=0 and result.report and result.report.get('failures',0)>0, label
 print(label+': detected by reviewed tests',flush=True)
