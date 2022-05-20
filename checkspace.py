#without if function
st="this  is  string  with  doubble  spaces."
ds=st.find("  ")
dss=st.replace("  ","$")
print(dss)
print(ds)
#with if function


if st.find("  "):
	print("true")
	dss=st.replace("  ","$")
	print(dss)
else:	
	print("flase")
