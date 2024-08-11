// READE ME//

I request the program be run in a console* for the best experience

Syntax - ORIGINS

This converter is based on the logic that you would find in a CAIE O-A level exam (2023).
As such, the syntax is quite simple:

	1 - INPUT / OUTPUT
	2 - IF THEN ELSE / ELSEIF...ENDIF
	3 - CASE OF (NOT ADDED) //Who the hell uses case of?
	4 - LOOPS
		- FOR TO NEXT
		- WHILE ENDWHILE
		- REPEAT UNTIL

	5 - PROCEDURE (BYREF & BYVAL) / FUNCTIONS
	6 - RECORD <DATA_TYPE> // limited to only 1 implementation
	7 - EXTRA FUNCTIONS PROVIDED BY CAIE exam board: [9618_s21_in_22.pdf](https://github.com/user-attachments/files/16571690/9618_s21_in_22.pdf)
	8 - Assignment of variables
	9 - Simple Arithmetic

	# I know that more things could be added, like array declarations of specific sizes, opening and closing files, but, I built this program based on what a student might want to 
 	# convert based on questions, and since files in questions contain virtual data, users won't ACTUALLY be able to skim the file and do something with it, tho adding the functionality 
  	# might be fun :)
   
	
Now the syntax of each point: 

	1. INPUT <variable>

	2. OUTPUT <text>, <variable> etc

	3. 			IF <condition> THEN
					<action>
				ELSEIF <condition> THEN
					<action_2>
				ELSE 
					<action_3>
				ENDIF

	4. LOOPS

		(i) 	FOR <counter-variable> <-- <start> TO <end> STEP <value | normally at 1>
					<action>
				NEXT <counter-variable>

		(ii) 	WHILE <condition>
					<action>
				ENDWHILE

	4	(c) 	REPEAT
					<action>
				UNTIL <condition>
				
	5.  (i) 	PROCEDURE <name>(<parameter_value> : <data_type>)
					<actions>
				ENDPROCEDURE
				
		(ii) 	PROCEDURE <name>(<BYREF or BYVAL> <parameter_value> : <data_type>)
					<actions>
				ENDPROCEDURE
				
		(iii)   FUNCTION <name>(<parameter_value> RETURNS <data_type>
					<actions>
				RETURN <var>
				ENDFUNCTION

	6. 	TYPE <record_name>
			DECLARE <var> : <data_type>
		END TYPE

	7.	read: [9618_s21_in_22.pdf](https://github.com/user-attachments/files/16571690/9618_s21_in_22.pdf)

	8. <var> <-- <var2>

	9. <var> <-- <var> MOD <var2> + <var3> / <var4>
