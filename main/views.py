from django.shortcuts import render

# Create your views here.

class CSP_Validate:

    def __init__(self, request):

        self.request = request

    def Validate_Default(self):

        if (str(self.request.POST.get('CSP-Default'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Default'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Default'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Default'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Default'))) == 'Data':
            return("'data'")

    def Validate_Script(self):

        if (str(self.request.POST.get('CSP-Script'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Script'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Script'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Script'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Script'))) == 'Data':
            return("'data'")
        elif (str(self.request.POST.get('CSP-Script'))) == 'Inline':
            return("'Unsafe-inline'")
        elif (str(self.request.POST.get('CSP-Script'))) == 'Eval':
            return("'Unsafe-Eval'")

    def Validate_Style(self):
    
        if (str(self.request.POST.get('CSP-Style'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Style'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Style'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Style'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Style'))) == 'Data':
            return("'data'")
        elif (str(self.request.POST.get('CSP-Style'))) == 'Inline':
            return("'Unsafe-inline'")

    def Validate_Image(self):
    
        if (str(self.request.POST.get('CSP-Image'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Image'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Image'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Image'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Image'))) == 'Data':
            return("'data'")

    def Validate_Font(self):
        
        if (str(self.request.POST.get('CSP-Font'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Font'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Font'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Font'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Font'))) == 'Data':
            return("'data'")

    def Validate_Connect(self):
        
        if (str(self.request.POST.get('CSP-Connect'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Connect'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Connect'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Connect'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Connect'))) == 'Data':
            return("'data'")

    def Validate_Media(self):
        
        if (str(self.request.POST.get('CSP-Media'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Media'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Media'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Media'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Media'))) == 'Data':
            return("'data'")

    def Validate_Object(self):
        
        if (str(self.request.POST.get('CSP-Object'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Object'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Object'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Object'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Object'))) == 'Data':
            return("'data'")

    def Validate_Frame(self):
        
        if (str(self.request.POST.get('CSP-Frame'))) == '':
            return('')
        elif (str(self.request.POST.get('CSP-Frame'))) == 'None':
            return("'none'")
        elif (str(self.request.POST.get('CSP-Frame'))) == 'All':
            return("'*'")
        elif (str(self.request.POST.get('CSP-Frame'))) == 'Self':
            return("'self'")
        elif (str(self.request.POST.get('CSP-Frame'))) == 'Data':
            return("'data'")
    
def home(request):

    return render(request, 'index.html')

def csp(request):

    obj = CSP_Validate(request)

    CSP_Output = '0'

    if not str(request.POST.get('CSP-Default-Host')):
        CSP_Default = obj.Validate_Default()
    else:
        CSP_Default = str(request.POST.get('CSP-Default-Host'))

    if not str(request.POST.get('CSP-Script-Host')):
        CSP_Script = obj.Validate_Script()
    else:
        CSP_Script = str(request.POST.get('CSP-Script-Host'))

    if not str(request.POST.get('CSP-Style-Host')):
        CSP_Style = obj.Validate_Style()
    else:
        CSP_Style = str(request.POST.get('CSP-Style-Host'))

    if not str(request.POST.get('CSP-Image-Host')):
        CSP_Image = obj.Validate_Image()
    else:
        CSP_Image = str(request.POST.get('CSP-Image-Host'))

    if not str(request.POST.get('CSP-Font-Host')):
        CSP_Font = obj.Validate_Font()
    else:
        CSP_Font = str(request.POST.get('CSP-Font-Host'))

    if not str(request.POST.get('CSP-Connect-Host')):
        CSP_Connect = obj.Validate_Connect()
    else:
        CSP_Connect = str(request.POST.get('CSP-Connect-Host'))

    if not str(request.POST.get('CSP-Media-Host')):
        CSP_Media = obj.Validate_Media()
    else:
        CSP_Media = str(request.POST.get('CSP-Media-Host'))

    if not str(request.POST.get('CSP-Object-Host')):
        CSP_Object = obj.Validate_Object()
    else:
        CSP_Object = str(request.POST.get('CSP-Object-Host'))

    if not str(request.POST.get('CSP-Frame-Host')):
        CSP_Frame = obj.Validate_Frame()
    else:
        CSP_Frame = str(request.POST.get('CSP-Frame-Host'))

    CSP_Report_URI = str(request.POST.get('CSP-Report-URI'))

    CSP_Report_Check = str(request.POST.get('CSP-Report-Check'))

    if (not CSP_Default and not CSP_Script and not CSP_Style and not CSP_Image and not CSP_Font and not CSP_Connect and not CSP_Media and not CSP_Object and not CSP_Frame and not CSP_Report_URI) :

        CSP_Output =  '0'

    elif CSP_Default == 'None':

        CSP_Output = '0'

    else :

        CSP_Output = '1'


    return render(request, 'csp.html', {'CSP_Output' : CSP_Output , 'CSP_Default' : CSP_Default , 'CSP_Script' : CSP_Script , 'CSP_Style' : CSP_Style , 'CSP_Image' : CSP_Image , 'CSP_Font' : CSP_Font , 'CSP_Connect' : CSP_Connect , 'CSP_Media' : CSP_Media , 'CSP_Object' : CSP_Object , 'CSP_Frame' : CSP_Frame , 'CSP_Report_URI' : CSP_Report_URI , 'CSP_Report_Check' : CSP_Report_Check})
    
def xframe(request):

    xframe_Output = ''
    xframe_Option = ''
    xframe_Conf = str(request.POST.get('x-frame-conf'))

    if str(request.POST.get('x-frame-option')) == '1':

        xframe_Output = '1'

        xframe_Option = 'DENY'

    elif str(request.POST.get('x-frame-option')) == '2':

        xframe_Output = '1'

        xframe_Option = 'SAMEORIGIN'

    else :

        xframe_Output = '0'

    return render(request, 'xframe.html' , {'xframe_Output' : xframe_Output , 'xframe_Option' : xframe_Option , 'xframe_Conf' : xframe_Conf})
    
def hsts(request):

    hsts_Output = '0'

    hsts_max_age = ''

    if request.POST.get('hsts-max-age') :

        hsts_max_age = str(request.POST.get('hsts-max-age'))

        hsts_Output = '1'
    
    hsts_includeSubDomains = str(request.POST.get('hsts-includeSubDomains'))

    hsts_preload = str(request.POST.get('hsts-preload'))
    
    return render(request, 'hsts.html' , {'hsts_Output' : hsts_Output , 'hsts_max_age' : hsts_max_age , 'hsts_includeSubDomains' : hsts_includeSubDomains , 'hsts_preload' : hsts_preload} )

def referrer(request):

    referrer_Output = '0'

    referrer_Option = str(request.POST.get('referrer-option'))

    if request.POST.get('referrer-option') and str(request.POST.get('referrer-option')) != '0' :
        
        referrer_Output = '1'
        
    return render(request, 'referrer.html' , {'referrer_Output' : referrer_Output , 'referrer_Option' : referrer_Option} )

def xcontent(request):

    return render(request, 'xcontent.html')

def xpermit(request):
    
    xpermit_Output = '0'

    xpermit_Option = str(request.POST.get('xpermit-option'))

    if request.POST.get('xpermit-option') and str(request.POST.get('xpermit-option')) != '0' :
        
        xpermit_Output = '1'
        
    return render(request, 'xpermit.html' , {'xpermit_Output' : xpermit_Output , 'xpermit_Option' : xpermit_Option} )

def clearsite(request):
    
    clearsite_Output = '0'

    clearsite_cache = str(request.POST.get('clearsite-cache'))

    clearsite_cookies = str(request.POST.get('clearsite-cookies'))

    clearsite_storage = str(request.POST.get('clearsite-storage'))

    clearsite_executionContexts = str(request.POST.get('clearsite-executionContexts'))

    clearsite_all = str(request.POST.get('clearsite-all'))

    if clearsite_cache == '1' or clearsite_cookies == '1' or clearsite_storage == '1' or clearsite_executionContexts == '1' or clearsite_all == '1'  :

        clearsite_Output = '1'
    
    return render(request, 'clearsite.html' , {'clearsite_Output' : clearsite_Output , 'clearsite_cache' : clearsite_cache , 'clearsite_cookies' : clearsite_cookies , 'clearsite_storage' : clearsite_storage , 'clearsite_executionContexts' : clearsite_executionContexts , 'clearsite_all' : clearsite_all} )

def coep(request):
    
    coep_Output = ''
    coep_Option = ''
    coep_report = str(request.POST.get('coep-report-only'))

    if str(request.POST.get('coep-option')) == '1':

        coep_Output = '1'

        coep_Option = 'unsafe-none'

    elif str(request.POST.get('coep-option')) == '2':

        coep_Output = '1'

        coep_Option = 'require-corp'

    else :

        coep_Output = '0'

    return render(request, 'coep.html' , {'coep_Output' : coep_Output , 'coep_Option' : coep_Option , 'coep_report' : coep_report})

def coop(request):
    
    coop_Output = ''
    coop_Option = ''
    coop_report = str(request.POST.get('coop-report-only'))

    if str(request.POST.get('coop-option')) == '1':

        coop_Output = '1'

        coop_Option = 'unsafe-none'

    elif str(request.POST.get('coop-option')) == '2':

        coop_Output = '1'

        coop_Option = 'same-origin-allow-popups'
    
    elif str(request.POST.get('coop-option')) == '3':
    
        coop_Output = '1'

        coop_Option = 'same-origin'

    else :

        coop_Output = '0'

    return render(request, 'coop.html' , {'coop_Output' : coop_Output , 'coop_Option' : coop_Option , 'coop_report' : coop_report})

def corp(request):
    
    corp_Output = ''
    corp_Option = ''
    corp_report = str(request.POST.get('corp-report-only'))

    if str(request.POST.get('corp-option')) == '1':

        corp_Output = '1'

        corp_Option = 'same-site'

    elif str(request.POST.get('corp-option')) == '2':

        corp_Output = '1'

        corp_Option = 'same-origin'
    
    elif str(request.POST.get('corp-option')) == '3':
    
        corp_Output = '1'

        corp_Option = 'cross-origin'

    else :

        corp_Output = '0'

    return render(request, 'corp.html' , {'corp_Output' : corp_Output , 'corp_Option' : corp_Option , 'corp_report' : corp_report})

def feature(request):
    
    feature_Output = ''
    feature_Option_1 = ''
    feature_Option_2 = ''
    # corp_report = str(request.POST.get('corp-report-only'))

    if request.POST.get('feature-option-1') and request.POST.get('feature-option-2') :

        if str(request.POST.get('feature-option-1')) != '0' and str(request.POST.get('feature-option-2')) != '0':

            feature_Output = '1'

            feature_Option_1 = str(request.POST.get('feature-option-1'))

            feature_Option_2 = str(request.POST.get('feature-option-2'))

    else :

        feature_Output = '0'

    return render(request, 'feature.html' , {'feature_Output' : feature_Output , 'feature_Option_1' : feature_Option_1 , 'feature_Option_2' : feature_Option_2})

def expect(request):
    
    expect_Output = '0'

    expect_max_age = ''

    expect_report_uri = ''

    uri = ''

    if request.POST.get('expect-max-age') :

        expect_max_age = str(request.POST.get('expect-max-age'))

        expect_Output = '1'

    if request.POST.get('expect-report-uri') :

        expect_report_uri = '1'

        uri = str(request.POST.get('expect-report-uri'))

    expect_enforce = str(request.POST.get('expect-enforce'))
    
    return render(request, 'expect.html' , {'expect_Output' : expect_Output , 'expect_max_age' : expect_max_age , 'expect_report_uri' : expect_report_uri , 'expect_enforce' : expect_enforce , 'uri' : uri} )