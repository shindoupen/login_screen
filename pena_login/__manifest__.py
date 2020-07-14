{
    "name"      : "PENA Custom Login Theme",
    "summary"   : """ Module for modified default odoo login page """,
    "version"       : "1.0",    
    "license"       : "LGPL-3",
    "depends"       : ["base","account"],
    "author"        : "Shindou",
    "category"      : "Themes",
    "images"        : ["pena_login,static/description/icon.png"],
    "website"       : "windu.blogz.id", 
    "support"       : "winduprimaesa@gmail.com",
    "depends"       : ["base"],
    "data"          : ["templates/pena_custom_login_page.xml",],

    'installable': True,
    'auto_install': False,
    'application': True,

}