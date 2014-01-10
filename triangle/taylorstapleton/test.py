#! /usr/bin/python

import subprocess

def testIso(debug):
	test_cases = { 'isosceles acute': [ '0' , '0' , '2' , '0', '1' , '4' ], 'isosceles obtuse': [ '0' , '0' , '4' , '0', '2' , '1' ], 'isosceles right': [ '0' , '0' , '2' , '0', '1' , '1' ] }

	toReturn = ""

	for expected_output, provided_input in test_cases.iteritems():
		output = subprocess.check_output( [ './triangle' ] + provided_input )
		if ( debug == "true" ):
			print("output = " + output)
			print( "expected = " + expected_output + "    actual = " + output )

		if ( output != expected_output+'\n' ):
			toReturn += expected_output.split()[1] + " "

	return toReturn

def testSca(debug):
        toReturn = ""
        output = subprocess.check_output(['./triangle' , '0' , '0' , '2' , '3', '3' , '1'])
        if(debug == "true"):
                print("output = " + output)
                print("expected = scalene acute    actual = " + output)
        if(output != "scalene acute\n"):
                toReturn += "acute "


        output = subprocess.check_output(['./triangle' , '0' , '0' , '4' , '4', '2' , '4'])
        if(debug == "true"):
                print("output = " + output)
                print("expected = scalene obtuse    actual = " + output)
        if(output != "scalene obtuse\n"):
                toReturn += "obtuse "


        output = subprocess.check_output(['./triangle' , '0' , '0' , '2' , '0', '0' , '4'])
        if(debug == "true"):
                print("output = " + output)
                print("expected = scalene right    actual = " + output)
        if(output != "scalene right\n"):
                toReturn += "right "

        return toReturn

def testNot(debug):
        toReturn = ""
        output = subprocess.check_output(['./triangle' , '0' , '0' , '1' , '1', '2' , '2'])
        if(debug == "true"):
                print("output = " + output)
                print("expected = not a triangle    actual = " + output)
        if(output != "not a triangle\n"):
                toReturn += "line "


        output = subprocess.check_output(['./triangle' , '0' , '0' , '0' , '0', '0' , '0'])
        if(debug == "true"):
                print("output = " + output)
                print("expected = not a triangle    actual = " + output)
        if(output != "not a triangle\n"):
                toReturn += "equal "

        return toReturn



def main():
	debug = "false"
	returnedValue = testIso(debug)
	if(returnedValue != ""):
		print("failed isosceles: " + returnedValue)

	returnedValue = testSca(debug)
        if(returnedValue != ""):
                print("failed scalene: " + returnedValue)
	
	returnedValue = testNot(debug)
        if(returnedValue != ""):
                print("failed not a triangle: " + returnedValue)


if __name__ == '__main__':
	main()

