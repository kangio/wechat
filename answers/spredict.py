#coding=utf-8
from  get_key import inaction,inscene,inask,getv,outbad
import sys
from scean import scenelib
sys.path.append('..')
from corpus_segment import CorpusSegement
from chatbot_integration import tmp_a
seg=CorpusSegement()
ab=tmp_a()
def predict(line):
    # reload(sys)
    # sys.setdefaultencoding('utf8')
    result=[]
    line1=line
    line1=line1.encode('utf-8')
    ab.predict(line1,result)
    line2=' '.join(seg.single_segment(line,hasOrigin=True))
    print line2
    dl = line2.split('####')
    for sc in scenelib:
        if inscene(dl[0], sc):
            # out.append(dl[1].strip() + getv(dl[0]))
            if inask(dl[0], sc):
                if inaction(dl[0], sc):
                    if outbad(dl[0], sc):
                        result.append(sc.ans)
    return result

pline=raw_input('输入问题：').decode('utf-8')
while pline!=u'q':
    res=predict(pline)
    if len(res)==0:
        print u'没发现答案'
    else:
        for i in res:
            print '10086：',i
    pline=raw_input('输入问题：').decode('utf-8')
