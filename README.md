# TB2J\_SIESTA\_TUTORIAL

## Useful links for TB2J
 Documentaion: https://TB2J.readthedocs.io

 Github: https://www.github.com/mailhexu/TB2J

 forum: https://groups.google.com/g/tb2j

## Files for running TB2J tutorial

  https://github.com/mailhexu/TB2J_TUTORIAL



## Install TB2J

Note: For this tutorial, you need to install sisl and netcdf4 alongside TB2J as they are required to read the SIESTA output in the netcdf format provided in the tutorial.

```
    pip install TB2J
```

## Notes:
```
  SaveHS True
```
  must be in the siesta input. 


## Examples in this tutorial:




### bcc Fe: in directory  bccFe\_siesta
  - basis usage of TB2J-SIESTA 

    In the DFT directory, use the command in getJ.sh to compute the exchange parameters.

  - Spin dynamics in bccFe (use example of MULTIBINIT)

    In the MULTIBINIT directory, run the command in run.sh 
    to run the monte carlo calculation. 

  - Magnon band structure (old implementation)


    In the MULTIBINIT directroy, run 

    ```
    TB2J_magnon.py --show
    ```

  to plot the magnon band structure.

  - Magnon band structure (new implementation, not available yet in the official TB2J)



### CrI3 collinear calculation:  in directory CrI3\_SIESTA\_collinear 
   - Another usage of TB2J-SIESTA
   - collinear spin calculation (SIESTA)
   - Computing isotropic exchange (TB2J)

   In the DFT directory, use the command in getJ.sh to compute the exchange parameters.

### CrI3 SOC calculation: in directory CrI3\_SIESTA\_SOC
This is an example of running TB2J-SIESTA with spin-orbit coupling (SOC) in SIESTA, which gives not only the exchange parameters but also the Dzyaloshinskii-Moriya interaction (DMI) parameters and anisotropic exchange.

    In this tutorial, three SIESTA calcualtions needs to be done, with the spin along the x, y, and z axis, respectively.

    After the DFT calculations, go to each directory and you can find the command of TB2J in getJ.sh script. 

    Then, we can run the command  in merge.sh to the the final exchange parameters.


###    CrI3\_SIESTA\_split\_SOC

This is an example for running the new TB2J noncollinear spin, in which there is no need to run three DFT calculations and merge the result. Instead it requires only a single DFT calculation. 


