# Trigonometric-Encryption
An Encryption that uses the Trigonometric Functions to encrypt text 


WARNING:
You have some equations: look for ">>>>>  gd2md-html alert:  equation..." in output.


WARNING:
Inline drawings not supported: look for ">>>>>  gd2md-html alert:  inline drawings..." in output.

* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 2; ALERTS: 38.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>
<a href="#gdcalert17">alert17</a>
<a href="#gdcalert18">alert18</a>
<a href="#gdcalert19">alert19</a>
<a href="#gdcalert20">alert20</a>
<a href="#gdcalert21">alert21</a>
<a href="#gdcalert22">alert22</a>
<a href="#gdcalert23">alert23</a>
<a href="#gdcalert24">alert24</a>
<a href="#gdcalert25">alert25</a>
<a href="#gdcalert26">alert26</a>
<a href="#gdcalert27">alert27</a>
<a href="#gdcalert28">alert28</a>
<a href="#gdcalert29">alert29</a>
<a href="#gdcalert30">alert30</a>
<a href="#gdcalert31">alert31</a>
<a href="#gdcalert32">alert32</a>
<a href="#gdcalert33">alert33</a>
<a href="#gdcalert34">alert34</a>
<a href="#gdcalert35">alert35</a>
<a href="#gdcalert36">alert36</a>
<a href="#gdcalert37">alert37</a>
<a href="#gdcalert38">alert38</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>
##

## <span style="text-decoration:underline;">Introduction</span>

With the growing reliance on computers and the Internet, data privacy is undoubtedly one of the most critical concerns of modern society. It may be argued that the majority of the global government processes have been computerized, and with this comes the growing importance of data encryption. Encryption is the mechanism by which information is scrambled to allow only approved parties to view it[^1]. Recently, the United States was the target of a suspected Russian cyber-attack, in which the State Department, the Treasury Department, Homeland Security, the National Security Administration and several others have been breached. It is suspected that the alleged hackers compromised and seized a significant amount of sensitive information, the most critical of which was nuclear technology[^2]. Taking this into account, it is plausible to conclude that data security and encryption are crucial for our current society. This increasing significance of cryptography, the art of encryption, served as inspiration for this investigation. 

With a view to the reader understanding this exploration, I shall first introduce some definitions. 


    Plain text = the original text that is to be encrypted


    Crypt or Cipher text = “text transformed from plaintext using an encryption algorithm”[^3]

In the following paper I will propose a simple trigonometry-based encryption system. The aim of the paper is to be able to successfully encrypt a text into an unrecognisable format and then decrypt it back to plain text. Since this is primarily a digital issue, the investigation will also present its findings in a code format using the Python programming language. It should be noted that the programming language used is irrelevant; because this inquiry is presenting an algorithm rather than a concrete solution, it can be recreated in any language.

The process of encryption that I am exploring in this paper is quite simple. Initially, several values which will define the different parameters for the tangent(tan) function are supplied by a user. Once given these values, the tangent function will be graphed in a way such that only one period of the graph can be seen. The letters of the alphabet will then be distributed on the _x _axis across the domain of one period of the function. The same will be done on the _y_-axis. Therefore, once an _x _value that has a letter linked to it, is processed through the tangent function, there will be a _y _value returned with another letter linked to it. The letters on the x axis or the will represent the pain text whereas the letters on the _y _axis or the letters corresponding to the output of the tangent function will be the crypt letter.  


## <span style="text-decoration:underline;">Process</span>

As the program initialises, the user is prompted to provide several values for the transformation formula of the tan graph. This follows the formula:

![Process][images/Process.png]

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



 Where:


    	a = Vertical stretch; (determined by the user)


    	b = cycles per wavelength; (determined by the user)


    	c = Horizontal translation; (calculated)


    	d = Vertical translation; (determined by the user)


    	x = the input value; (determined by the user)

Determining the best possible parameters is important for the encryption to work. Starting with _a(vertical stretch)_, it was given an arbitrary value of _10_. As the first value to be determined by the user, it can be any real number. The _p(period) _parameter needs to have a value such that all the letters in the alphabet and the pseudo-letter “_space_” can fit in with minimum difference of _1 _between their subsequent values. Therefore, it needs to be a value greater than _54_(i.e. _p <span style="text-decoration:underline;">&lt;</span> (27*2)_). For ease of calculation, it was given a magnitude of _100_. The horizontal translation(_c) _value was important as it determined the horizontal position of the graph. The basic tan function has one period centered on the origin. This encryption process required a period of the tan function with all its values being positive. Since it was centered on the origin and the period of the tan graph is symmetrical, The horizontal translation had to be exactly half of the period. The vertical translation(_d_) had no significance in the encryption process and can be given any value. 


## Encryption

Before the encryption process begins, the program assigns an index value to each letter in the alphabet, eg “space” = 0, a = 1, b = 2, c = 3, …, z = 27. When this is finished, the length of the tan wave is taken and all the letters are uniformly distributed around it. This can be seen 

in the code below.

At line 40, the “for” command loops through every letter in the alphabet and assigns each one a unique value by dividing the period of the tan graph by the total number of letters (i.e. 27 including “space”) and multiplying this value by their index value. In formulaic terms this

would look like this: 



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Where, _“index [letter]”_ is the index value that corresponds to that specific letter. After this, the x values produced by this formula are substituted into the tan graph formula to find the_ y _value they correspond with.

**<span style="text-decoration:underline;">Sample calculation</span>**:



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



The rest has been calculated and presented in table and graph format below. 

**<span style="text-decoration:underline;"> Data table 1</span>**

After this calculation, the algorithm will continue to do the same for the y values. The letters in the alphabet would be evenly distributed around the y-axis such that the y-values determined using the tan function can be converted into a letter, essentially forming the corresponding crypt letter or a given _input value(x)_. One may already observe that the approach suggested above would not allow for a proper encryption and decryption procedure, as the _y-_values output from the_ x-_values passing through the tan function have an large increase in distance from each other, thus, for this case, the crypt letters will have to be spaced apart on the y-axis from _(-206, 206)_ – rounded values. This is a total distance of _412_ and once calculated, each consecutive crypt letter would need to have a value difference of_ ~ 16_, which can be derived by following the calculation below. 

Since we want to distribute_ 27_ values evenly across the _y-_axis, we can just take the central or median value away from the indexes of all the values. The central value between 0 and _27_ is exactly _13_, therefore

<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

, where s = separation.

In an instance where_ s = 1_, we would get the following values: 


    **<span style="text-decoration:underline;">Data table 2</span>**

This formula allows for the even spread of the letters across the _y _axis. The difference between these letters can be determined by the value of _“s”_. By rearranging the formula we can calculate the _s_ value required for the values in _data table 1_. The picture on the right is the same calculation but in the form of a code.

Let’s take the character or letter [_space_] as it has the highest _Y-Value_



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



An _s_ value of _16_ would give the following:

 **<span style="text-decoration:underline;">Data table 3</span>**

Unfortunately, this cant be used to encrypt and decrypt as there is a substantially increasing distance between the values. For example, all the values highlighted in data table 1 can only be encrypted to the letters highlighted in_ data table 3_. This was an annoying problem that was encountered, but a solution was found. This solution was to take away the ends of the tan graph which would allow values to have a more consistent difference. Different methods were attempted to do this but the most effective was the following:

The period (_100 units_) defines the entire length of one period of the tan wave, and let’s assume that the stretched ends of the tan wave constitute about 20 units of its length. Using this assumption we can modify the _x-_values originally assigned to the letters to effectively cut out the, for a lack of a better description, the “_stretched ends_''. So, since _20_ units is _20%_ percent of the total length and there are _2_ of them, that’s a total of _40%_ of the graph which is composed of the “_stretched ends_”. We can start by just multiplying the period by _60%_ to take away _40%_ of the graph from the right side. This will look like this:

Figure 3, graph with one cut end

As we can observe, _40%_ of its length was taken away from the right but since only _20%_ of it is what we considered the “stretched end” we can increase all preceding x values by _20%_ of the period to essentially shift all the values and find just take the middle of the tan graph. 

This would look like this: 

Figure 4, middle of a tan graph

From here, we can calculate the exact _c_ value required to centre the graph by adding the highest and lowest _x_ values together and dividing by _2_. This would be calculated as:



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





Due to our focus on the middle of the tan graph, we would now have a new set of values. 

**<span style="text-decoration:underline;">Data Table 4</span>**



<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline drawings not supported directly from Docs. You may want to copy the inline drawing to a standalone drawing and export by reference. See <a href="https://github.com/evbacher/gd2md-html/wiki/Google-Drawings-by-reference">Google Drawings by reference</a> for details. The img URL below is a placeholder. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![drawing](https://docs.google.com/drawings/d/12345/export/png)

Since the values have a much smaller difference between each other now, we can use the formula stated earlier to assign letters on the_ y _axis. The maximum_ y _value with an _s_ value of _1_ is _13_ therefore the s value can be slightly increased to fit the data. In this case, an _s _value of 1.15 was found to be the best for encryption and decryption.

**<span style="text-decoration:underline;">Data table 5</span>**



<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline drawings not supported directly from Docs. You may want to copy the inline drawing to a standalone drawing and export by reference. See <a href="https://github.com/evbacher/gd2md-html/wiki/Google-Drawings-by-reference">Google Drawings by reference</a> for details. The img URL below is a placeholder. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![drawing](https://docs.google.com/drawings/d/12345/export/png)

Now that the letters on both the _x_ and _y_ axis have been unique values we can start the encryption and decryption process. This process in the code is defined using a function called “encrypt (plaintext)” which takes a plain text as an input and returns the crypt text.

The “_for_” loop in line 68 goes through the plain text provided and splits it into its constituent letters.  Once it obtains the letters, which it refers to as “_char_”, it looks up their corresponding _x _value which is defined in_ data table 4_.

It then puts the _x_ value that was obtained into a tan function. The _y _value that is obtained after this is saved as a variable named “_yval_”. The function then looks at _data table 5_ and uses a function I created called “_approximate” _to find the closest value to “_yval_”. 

The approximate function takes in two arguments, a list of numbers and a value. It then loops through the list and takes away the value from each number. It attempts to find the number which has the least absolute difference with the input value and returns that number. 

Sample Calculation:  The plain text, “_this is a maths assessment_”, starts with a “_t_” so let’s use that for this example. 



<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Now that we have the _yval_, we can start the approximation process. Since it’s hard to show this using formula, it will be displayed in table format. 

 **<span style="text-decoration:underline;">Data table 5 </span>**

This is a representation of what the approximate function does. From what we can see, the letter _“s”_ has a _y _value with the least absolute difference to the _y _value of _“t”_ so, _“t”_ gets encrypted into _“s”_. This process will then be repeated for every letter to produce the crypt text. The full length of the plain text .

**<span style="text-decoration:underline;">Data table 6</span>**

**<span style="text-decoration:underline;">Decryption process </span>**

The decryption process is the exact reverse of the encryption process. We take the crypt text and find its corresponding _y _value from data table 5, then we utilise the inverse function to find an x value that would correspond with that value. The inverse function is:



<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Since this function will not output an exact match to the predetermined_ x _values which letters on the_ x _axis already have, its output will go through the approximating function. In code, this would look like this:

**<span style="text-decoration:underline;">Sample Calculation </span>**

Crypt text = “_sijr jr a masir jnsfqnal arrfrrmfns_”

Let’s take the first letter “_s_” 



<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Since the x value of “_64.44444444_” is equal to the_ x_ value of_ _“_t_”, “_s_” will be decrypted to “_t_”. 

**Other examples: **


                                    Plain text “This was an interesting experiment”


                                    

<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


Plain text “cryptography was fun to learn”



<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


Plain text “Some errors can be observed”



<p id="gdcalert36" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert37">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


Plain text “These errors exist around the middle of the tan graph”



<p id="gdcalert37" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert38">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


The errors observed above, more specifically with the letter “o”, is the result of the “squashed” middle of the tan graph. The letters “k, l, m, n, o” have a difference that is under 1.15 thus two of the letters get encrypted to the same letter. In this case, the letter o and n had too close of a value and the approximation function encrypted “o” to “n” when encrypting back, since the values were close, it returned “n” rather than “o”. This can be demonstrated by looking at the following example encryption of the plain text “klmno”



<p id="gdcalert38" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline drawings not supported directly from Docs. You may want to copy the inline drawing to a standalone drawing and export by reference. See <a href="https://github.com/evbacher/gd2md-html/wiki/Google-Drawings-by-reference">Google Drawings by reference</a> for details. The img URL below is a placeholder. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert39">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![drawing](https://docs.google.com/drawings/d/12345/export/png)

**<span style="text-decoration:underline;">Conclusion</span>**

Overall it can be concluded that, whilst interesting, it's ultimately impossible to create such an encryption system that utilises the trigonometric functions without error. Here, as I tried to use the tan function, some restraints it had such as its “stretched ends” and “squashed middle” caused many errors in the encryption and decryption process. The way in which I was able to tackle these problems was by cutting out the ends, which ultimately made it more of a linear graph with a slight curve. This meant that, during encryption, for letters such as “a” or “z” there was no change whatsoever and the rest of the letters were just offset by one letter either forwards or backwards to form the crypt text. This conclusion, therefore, begs the question, what is the most optimum function for this process?

For a graph based encryption process such as the one I am trying to make, the function used passing the horizontal line test is critical. Using functions such as a sin function would ultimately not work as there are multiple x values which correspond to one y value. Even when taking one of its periods like we did for the tan graph, most y values correspond to at least two different values with an exception of y = 0 corresponding to three and  y = 1 which only corresponds to one x value as they represent the peak of the sin wave. Another way to interpret this is to say that the inverse of the function used must pass the horizontal line test. 

The figure on the left shows how the sine graph fails the vertical line test. One horizontal line intersects the graph at two points which are indicated by the red dots. This can be understood to mean that this function has multiple x values for corresponding to a single y value. Therefore, using this in the encryption process outlined above would be impossible. This would also eliminate the cosine function since it shares the same limitations as the sine function. 

However, the horizontal test isn't the only requirement for graphs to be used for this encryption system. There is the problem that arises as a graph curve. As seen above in this investigation from the “stretching ends'' and the “squashed middle”. These caused some problems when attempting to encrypt due to either a too big or too little of a difference in the value assigned to the different letters. This would, therefore, eliminate all exponential or  logarithmic functions which means that all the functions I have covered as part of my Maths Analysis and Approaches course cant be used for this encryption process. Other fully functioning graph based encryption algorithms exist (i.e. Elliptic curve encryption[^4]) but the math behind it is entirely outside the Maths AA syllabus and too complicated to effectively explain in such a short paper. Therefore, this investigation can be concluded with the understanding that there is an encryption algorithm that could be made using simple trigonometric graphs, though not fully functional, it works nonetheless. 

**<span style="text-decoration:underline;">Bibliography</span>**


        Loshin, P. (2019). What is encryption? SearchSecurity. https://searchsecurity.techtarget.com/definition/encryption


        Sanger, D.E. (2020). Russian Hackers Broke Into Federal Agencies, U.S. Officials Suspect. The New York Times. [online] 13 Dec. Available at: [https://www.nytimes.com/2020/12/13/us/politics/russian-hackers-us-government-treasury-commerce.html](https://www.nytimes.com/2020/12/13/us/politics/russian-hackers-us-government-treasury-commerce.html).


        Sullivan, N. (2013, October 24). A (Relatively Easy To Understand) Primer on Elliptic Curve Cryptography. The Cloudflare Blog; The Cloudflare Blog. [https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     Loshin, P. (2019). What is encryption? SearchSecurity. 

[^2]:
     Sanger, D.E. (2020). Russian Hackers Broke Into Federal Agencies, U.S. Officials Suspect. _The New York Times_. [online] 13 Dec. 

[^3]:
     Rosencrance, L. (2020, April). What is Ciphertext? WhatIs.com. https://whatis.techtarget.com/definition/ciphertext#:~:text=Ciphertext%20is%20encrypted%20text%20transformed

[^4]:
     Sullivan, N. (2013, October 24). A (Relatively Easy To Understand) Primer on Elliptic Curve Cryptography. The Cloudflare Blog; The Cloudflare Blog.
