# coding=utf-8
# from django.http import HttpResponse
from answers.get_key import inaction,inscene,inask,getv,outbad
from answers.scean import scenelib
from answers.corpus_segment import CorpusSegement
from answers.chatbot_integration import tmp_a
import codecs
# from tupu.MatchOnline import Match
seg=CorpusSegement()

ab=tmp_a()


def answer(line):
    result = []
    ans='!'
    if len(line) > 0:
        line1 = line
        # line1 = line1.encode('utf-8')
        ab.predict(line1, result)
        # print(result)
        line2 = ' '.join(seg.single_segment(line, hasOrigin=True))
        print(line2)
        dl = line2.split('####')
        for sc in scenelib:
            if inscene(dl[0], sc):
                # out.append(dl[1].strip() + getv(dl[0]))
                if inask(dl[0], sc):
                    if inaction(dl[0], sc):
                        if outbad(dl[0], sc):
                            result.append(sc.ans)
        # if '宽带' in line:
        #     line3 = line
        #     kd = Match(line3)
        #     for i in kd:
        #         result.append('图谱结果：' + i)

        if len(result) == 0:
            ans = '^_^'
        else:
            ans = '\n'.join(result)
    return ans

# print(answer('我还剩多少话费'))
