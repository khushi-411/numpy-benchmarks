### Errors

1. 
```
Traceback (most recent call last):
  File "/home/khushi/Documents/Quansight-Intern/pierre/pierre-4/acc_numba-2.py", line 104, in <module>
    cProfile.run('numba_loop(time_step, number_of_steps, masses, positions, velocities)')
  File "/usr/lib/python3.9/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/usr/lib/python3.9/profile.py", line 53, in run
    prof.run(statement)
  File "/usr/lib/python3.9/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/usr/lib/python3.9/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 1, in <module>
  File "/home/khushi/.local/lib/python3.9/site-packages/numba/core/dispatcher.py", line 482, in _compile_for_args
    error_rewrite(e, 'typing')
  File "/home/khushi/.local/lib/python3.9/site-packages/numba/core/dispatcher.py", line 423, in error_rewrite
    raise e.with_traceback(None)
numba.core.errors.TypingError: Failed in nopython mode pipeline (step: nopython frontend)
No implementation of function Function(<built-in function zeros>) found for signature:
 
 >>> zeros(UniTuple(int64 x 2), dtype=Function(<class 'float'>))
 
There are 4 candidate implementations:
   - Of which 4 did not match due to:
   Overload in function '_OverloadWrapper._build.<locals>.ol_generated': File: numba/core/overload_glue.py: Line 131.
     With argument(s): '(UniTuple(int64 x 2), dtype=Function(<class 'float'>))':
    Rejected as the implementation raised a specific error:
      TypingError: Failed in nopython mode pipeline (step: nopython frontend)
    No implementation of function Function(<intrinsic stub>) found for signature:
     
     >>> stub(UniTuple(int64 x 2), Function(<class 'float'>))
     
    There are 2 candidate implementations:
      - Of which 2 did not match due to:
      Intrinsic of function 'stub': File: numba/core/overload_glue.py: Line 35.
        With argument(s): '(UniTuple(int64 x 2), Function(<class 'float'>))':
       No match.
    
    During: resolving callee type: Function(<intrinsic stub>)
    During: typing of call at <string> (3)
    
    
    File "<string>", line 3:
    <source missing, REPL/exec in use?>

  raised from /home/khushi/.local/lib/python3.9/site-packages/numba/core/typeinfer.py:1074

During: resolving callee type: Function(<built-in function zeros>)
During: typing of call at /home/khushi/Documents/Quansight-Intern/pierre/pierre-4/acc_numba-2.py (54)


File "acc_numba-2.py", line 54:
def numba_loop(
    <source elided>
    
    accelerations = np.zeros(positions.shape, dtype = float)
    ^
```

How to resolve?

