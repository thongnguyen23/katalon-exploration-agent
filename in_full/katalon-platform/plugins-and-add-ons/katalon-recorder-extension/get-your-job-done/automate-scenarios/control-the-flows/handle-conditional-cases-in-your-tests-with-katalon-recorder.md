---
hide_title: true
title: Handle conditional cases in your tests with Katalon Recorder
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handle conditional cases in your tests with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder supports the following flow control methods: <ul className="ul"><li className="li"><p className="p">Branching</p></li><li className="li"><p className="p">Loops</p></li></ul></div>
    

## <a id="id_1" class="anchor_top_offset"/>Branching

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Conditional branching allows your test to behave differently   based on certain conditions.</p> 
    
                  
      

### <a id="id_2" class="anchor_top_offset"/>if

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">if</code> command opens a conditional branch. The   target of an <code className="ph codeph">if</code> command is an expression that   evaluates to either <code className="ph codeph">true</code> or <code className="ph codeph">false</code>. The   expression can be a JavaScript expression with variables. If the   expression evaluates to <code className="ph codeph">true</code>, all the steps following   <code className="ph codeph">if</code> will be executed until a <code className="ph codeph">else if</code>,   <code className="ph codeph">else</code> or <code className="ph codeph">endif</code> command is found.</p> 
      
    
      

### <a id="id_3" class="anchor_top_offset"/>else if

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">elseif</code> command is similar to the   <code className="ph codeph">if</code> command. If the steps between <code className="ph codeph">if</code> and   <code className="ph codeph">elseif</code> are not executed, the expression in   <code className="ph codeph">elseif</code> will be evaluated. If the expression evaluates   to <code className="ph codeph">true</code>, all commands following <code className="ph codeph">elseif</code>   will be executed until a <code className="ph codeph">else if</code>, <code className="ph codeph">else</code>,   or <code className="ph codeph">endif</code> command is found.</p> 
      
    
      

### <a id="id_4" class="anchor_top_offset"/>else

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">else</code> command usually follows the   <code className="ph codeph">if</code> command. If the steps between <code className="ph codeph">if</code> and   <code className="ph codeph">else</code> are not executed, the steps following   <code className="ph codeph">else</code> will be executed until a <code className="ph codeph">endif</code>   command is found.</p> 
      
    
      

### <a id="id_5" class="anchor_top_offset"/>endif

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">endif</code> command terminates the conditional   branching block. You need to add <code className="ph codeph">endif</code> to your test,   otherwise you will get an error message.</p> 
      
    
    

## <a id="id_6" class="anchor_top_offset"/>Looping

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Looping allows you to repeat steps until a condition is met.</p> 
    
          
      

### <a id="id_7" class="anchor_top_offset"/>while

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">while</code> command starts a loop. The target of a   <code className="ph codeph">while</code> command is an expression that evaluates to   either <code className="ph codeph">true</code> or <code className="ph codeph">false</code>. The expression can   be a JavaScript with variables. If the expression evaluates to   <code className="ph codeph">true</code>, the steps following <code className="ph codeph">while</code> will be   executed until <code className="ph codeph">endwhile</code> is found and the expression   evaluates again. The steps between <code className="ph codeph">while</code> and   <code className="ph codeph">endwhile</code> will be executed repeatedly until the   expression evaluates to <code className="ph codeph">false</code>.</p> 
      
    
      

### <a id="id_8" class="anchor_top_offset"/>endWhile

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">endwhile</code> command terminates the looping   branching block. You need to add <code className="ph codeph">endwhile</code> to your   test, otherwise you will get an error message.</p> 
      
    

## <a id="id_9" class="anchor_top_offset"/>Sample Projects

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder comes with some sample projects (templates) to
  help you get started with flow controls.<ol className="ol"><li className="li"><p className="p">In Katalon Recorder, go
        to Templates.</p></li><li className="li"><p className="p">Choose <em className="ph i">Conditional and loops</em> from the
        left-side bar.</p></li><li className="li"><p className="p">Check the sample projects.</p></li><li className="li"><p className="p">Click on the
        <strong className="ph b">Add Templates</strong></p></li></ol> </div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You should see the sample projects are added to your   workspace.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">See also</strong>:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-recorder-extension/get-your-job-done/automate-scenarios/control-the-flows/how-to-use-control-flow-commands-in-a-test-case-in-katalon-recorder">How       to Use Control Flow commands in a Test Case</a>   </li></ul> 
