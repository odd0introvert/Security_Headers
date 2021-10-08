from django.urls import path
from . import views 

urlpatterns = [
	path('',views.home, name='Homepage'),
    path('/',views.home, name='Homepage'),
    path('content-security-policy',views.csp, name='content-security-policy'),
    path('content-security-policy/',views.csp, name='content-security-policy'),
    path('X-Frame-Options',views.xframe, name='X-Frame-Options'),
    path('X-Frame-Options/',views.xframe, name='X-Frame-Options'),
    path('HTTP-strict-transport-security',views.hsts, name='HTTP-strict-transport-security'),
    path('HTTP-strict-transport-security/',views.hsts, name='HTTP-strict-transport-security'),
    path('Referrer-Policy',views.referrer, name='Referrer-Policy'),
    path('Referrer-Policy/',views.referrer, name='Referrer-Policy'),
    path('X-Content-Type-Options',views.xcontent, name='X-Content-Type-Options'),
    path('X-Content-Type-Options/',views.xcontent, name='X-Content-Type-Options'),
    path('X-Permitted-Cross-Domain-Policies',views.xpermit, name='X-Permitted-Cross-Domain-Policies'),
    path('X-Permitted-Cross-Domain-Policies/',views.xpermit, name='X-Permitted-Cross-Domain-Policies'),
    path('Clear-Site-Data',views.clearsite, name='Clear-Site-Data'),
    path('Clear-Site-Data/',views.clearsite, name='Clear-Site-Data'),
    path('Cross-Origin-Embedder-Policy',views.coep, name='Cross-Origin-Embedder-Policy'),
    path('Cross-Origin-Embedder-Policy/',views.coep, name='Cross-Origin-Embedder-Policy'),
    path('Cross-Origin-Opener-Policy',views.coop, name='Cross-Origin-Opener-Policy'),
    path('Cross-Origin-Opener-Policy/',views.coop, name='Cross-Origin-Opener-Policy'),
    path('Cross-Origin-Resource-Policy',views.corp, name='Cross-Origin-Resource-Policy'),
    path('Cross-Origin-Resource-Policy/',views.corp, name='Cross-Origin-Resource-Policy'),
    path('Feature-Policy',views.feature, name='Feature-Policy'),
    path('Feature-Policy/',views.feature, name='Feature-Policy'),
    path('Expect-CT',views.expect, name='Expect-CT'),
    path('Expect-CT/',views.expect, name='Expect-CT')
]
