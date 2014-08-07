country-calling-flag
====================

this is a tool to build the json information you want

check the build.py

###run
	$ python build.py

### result
**country.json ** for your project

the default result is 

	{
	“call”:”86”,
	”ch”:”\u4e2d\u56fd”,
	“en”:”china”,
	”ja”:”\u4e2d\u56fd”
	}
	
you can change the build.py for your project



###this project is based on

https://github.com/tellnes/country-flags

and 

https://github.com/mledoze/countries

###for the flag

there is a tool resize.py to resize the flag size, it is base on python PIL
  
 	pip install pillow 

### how to use
    glue ./flag-icon/ --recursive ./css/ --margin=5 --retina  --namespace= --watch
build a css spirit for the icons

### demo
there is a demo :demo.hmtl
