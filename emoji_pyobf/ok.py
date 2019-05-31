#!/usr/bin/env python
# Decompiled By https://mbasic.facebook.com/achmad.luthfi.hadi.3

import argparse #line:3
from collections import OrderedDict #line:4
from pprint import pformat #line:5
__created__ ='mR.C0c3nTz_404'#line:7
__copyright__ ='Copyright (c) 2019, Cocentz'#line:8
__youtube__ ='Youtube : Cocentz 404'#line:9
try :#line:10
    range =xrange #line:11
except NameError :#line:12
    pass #line:13
EMOTICONS =[':)',':D',':P',':S',':(','=)','=/',':/',':{',';)']#line:15
MAX_STR_LEN =70 #line:16
def run_argparse ():#line:19
    O00O0OO0O0O0OOOO0 =argparse .ArgumentParser (description ='''
 Obfuscate your python script by converting an input script to an output script
 that functions the same (hopefully) with encodes the script as emoji icons. Created: mR.C0c3ntz_404,Copyright (c) 2019,youtube: Cocentz 404''')#line:22
    O00O0OO0O0O0OOOO0 .add_argument ('-i','--input',required =True ,help ='input python script name')#line:24
    O00O0OO0O0O0OOOO0 .add_argument ('-o','--output',required =True ,help ='output python script name')#line:25
    return O00O0OO0O0O0OOOO0 .parse_args ()#line:26
def chunk_string (O000O00O0OOOO0000 ,O0OOOOO000O00OO00 ):#line:29
    return '\n'.join ('{}\\'.format (O000O00O0OOOO0000 [OOO0O0O0O0000OOO0 :OOO0O0O0O0000OOO0 +O0OOOOO000O00OO00 ])for OOO0O0O0O0000OOO0 in range (0 ,len (O000O00O0OOOO0000 ),O0OOOOO000O00OO00 )).rstrip ('\\')#line:31
def encode_string (OO0O000OO0O00OO00 ,OO0O0O0O00000O0O0 ):#line:34
    ""#line:35
    O00O00OO00O0O0O00 =OrderedDict (enumerate (OO0O0O0O00000O0O0 ))#line:38
    O0000O00O00OOO00O =OrderedDict ((OOOOO000O0OOO00OO ,O0OO00O0O000OOOO0 )for O0OO00O0O000OOOO0 ,OOOOO000O0OOO00OO in O00O00OO00O0O0O00 .items ())#line:39
    return ('from collections import OrderedDict\n' '# Obfuscate By mR.Coc3nTz_404\n' '# Youtube : Cocentz 404\n' '# Contact : +6285218219161\n' '# Thankz To My T34M BL4€K_AB4B1L_C0D3D\n' 'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n' '"{}"\n.split("  ")])))\n'.format (pformat (O0000O00O00OOO00O ),chunk_string ('  '.join (' '.join (O00O00OO00O0O0O00 [int (O00O00OO00O0OO0O0 )]for O00O00OO00O0OO0O0 in str (ord (OO00000O000000O0O )))for OO00000O000000O0O in OO0O000OO0O00OO00 ),MAX_STR_LEN )))#line:47
def main (O0O0O000O0O000O00 ,OO000OO000OO00OO0 ):#line:50
    ""#line:51
    with open (O0O0O000O0O000O00 )as OO0O0000OO00OOO0O ,open (OO000OO000OO00OO0 ,'w')as O00O00OOOO0OO0000 :#line:52
        O00O00OOOO0OO0000 .write (encode_string (OO0O0000OO00OOO0O .read (),EMOTICONS ))#line:54
if __name__ =='__main__':#line:57
    args =run_argparse ()#line:58
    main (args .input ,args .output )#line:59

