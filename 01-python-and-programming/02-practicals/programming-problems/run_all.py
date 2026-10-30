from pathlib import Path
import subprocess,sys
files=sorted(p for p in Path(__file__).parent.glob('[0-9][0-9]-*.py'))
for p in files:
    result=subprocess.run([sys.executable,str(p)],capture_output=True,text=True)
    if result.returncode:raise RuntimeError(str(p)+'\n'+result.stdout+result.stderr)
print('Passed',len(files),'programming solutions with their embedded assertions')
