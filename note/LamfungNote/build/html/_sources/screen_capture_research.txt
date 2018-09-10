Screen capture research
=======================

FAQ
---

#. DX is quicker than GDI?

::

 In my Impression, the GDI approach and the DX approach are different in its nature. 
 painting using GDI applies the FLUSH method, 
 the FLUSH approach draws the frame then clear it and redraw another frame in the same buffer, 
 this will result in flickering in games require high frame rate.
 
 WHY DX quicker? 
 in DX (or graphics world), a more mature method called double buffer rendering is applied, 
 where two buffers are present, when present the front buffer to the hardware, 
 you can render to the other buffer as well, then after the frame 1 is finished rendering, 
 the system swap to the other buffer( locking it for presenting to hardware , and release the previous buffer ), 
 in this way the rendering inefficiency is greatly improved.
 
 WHY turning down hardware acceleration quicker? 
 although with double buffer rendering, the FPS is improved, but the time for rendering is still limited. 
 modern graphic hardware usually involves a lot of optimization during rendering typically like anti-aliasing, 
 this is very computation intensive, if you don't require that high quality graphics, 
 of course you can just disable this option. and this will save you some time.



Reference
---------

#. https://stackoverflow.com/questions/5069104/fastest-method-of-screen-capturing
#. https://www.codeproject.com/Articles/5051/Various-methods-for-capturing-the-screen

