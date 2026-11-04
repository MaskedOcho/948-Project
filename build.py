import re,sys
src=open('src-artifact.html').read()
P='node_modules/three/'
m={'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js':P+'build/three.min.js'}
def rep(mo):
    u=mo.group(1)
    f=m.get(u) or P+u.split('three@0.128.0/')[1]
    return '<script>'+open(f).read().replace('</script','<\\/script')+'</script>'
out=re.sub(r'<script src="([^"]+)"></script>',rep,src)
head='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
reset='<style>html{color-scheme:light}body{margin:0;font:14px/1.45 system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>\n'
open(sys.argv[1] if len(sys.argv)>1 else 'index.html','w').write(head+reset+'</head>\n<body>\n'+out+'\n</body>\n</html>\n')
