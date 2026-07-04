# P04 Pixel-Measured Perspective Redraw Data

This pass detects source edges, runs a Hough line transform, extends detected line equations, and solves vanishing points from those detected lines.
Coordinates are normalized to the displayed crop for each source image.

## 1. Arcade Capriccio
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Arcade_Capriccio_MET_DP836399.jpg`
- Crop: `(0.02, 0.03, 0.98, 0.97)`
- Edge pixels used: `44191`
- Hough lines kept: `95`
- Perspective lines used for VP: `10`
- Solved VP: `(0.461698, 0.553743)`
- VP residual mean/max: `18.641px` / `32.259px` on the processing crop
- Perspective measurement lines:
  - L1: endpoints `(0.948378, 0.052997) -> (0.116996, 0.847623)`; angle `-147.000 deg`; votes `268`; support `431`; span `930.8px`; line `-0.69094619x + -0.72290620y + 0.69359007 = 0`; VP residual `24.180px`
  - L2: endpoints `(0.953894, 0.830491) -> (0.021817, 0.358137)`; angle `+161.000 deg`; votes `226`; support `371`; span `925.7px`; line `0.45204300x + -0.89199615y + 0.30959423 = 0`; VP residual `22.903px`
  - L3: endpoints `(0.824628, 0.966871) -> (0.051430, 0.077782)`; angle `+142.000 deg`; votes `224`; support `353`; span `921.3px`; line `0.75457328x + -0.65621579y + 0.01223408 = 0`; VP residual `2.591px`
  - L4: endpoints `(0.820693, 0.967854) -> (0.042471, 0.104751)`; angle `+143.000 deg`; votes `219`; support `338`; span `915.0px`; line `0.74268244x + -0.66964378y + 0.03860312 = 0`; VP residual `10.046px`
  - L5: endpoints `(0.910031, 0.323331) -> (0.017065, 0.854325)`; angle `-158.000 deg`; votes `275`; support `447`; span `904.3px`; line `-0.51110453x + -0.85951856y + 0.74303024 = 0`; VP residual `29.235px`
  - L6: endpoints `(0.821646, 0.958535) -> (0.102147, 0.038005)`; angle `+139.000 deg`; votes `220`; support `369`; span `895.2px`; line `0.78788542x + -0.61582186y + -0.05707587 = 0`; VP residual `32.259px`
  - L7: endpoints `(0.800513, 0.912473) -> (0.071624, 0.043762)`; angle `+141.000 deg`; votes `223`; support `357`; span `880.7px`; line `0.76606460x + -0.64276359y + -0.02674020 = 0`; VP residual `27.237px`
  - L8: endpoints `(0.811703, 0.946285) -> (0.071590, 0.183557)`; angle `+145.000 deg`; votes `241`; support `360`; span `848.4px`; line `0.71766622x + -0.69638725y + 0.07644920 = 0`; VP residual `20.844px`
  - L9: endpoints `(0.795908, 0.067886) -> (0.137879, 0.971007)`; angle `-137.000 deg`; votes `253`; support `419`; span `844.9px`; line `-0.80821902x + -0.58888201y + 0.68324539 = 0`; VP residual `15.038px`
  - L10: endpoints `(0.871545, 0.095891) -> (0.154730, 0.890889)`; angle `-143.000 deg`; votes `257`; support `413`; span `842.8px`; line `-0.74268244x + -0.66964378y + 0.71149379 = 0`; VP residual `2.080px`

## 2. Palace Fantasy
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Palace_Fantasy_NationalTrust.jpg`
- Crop: `(0.0, 0.0, 1.0, 1.0)`
- Edge pixels used: `27267`
- Hough lines kept: `95`
- Perspective lines used for VP: `10`
- Solved VP: `(0.485996, 0.595118)`
- VP residual mean/max: `14.295px` / `38.915px` on the processing crop
- Perspective measurement lines:
  - L1: endpoints `(0.973281, 0.506128) -> (0.043777, 0.697065)`; angle `-171.000 deg`; votes `196`; support `312`; span `883.7px`; line `-0.20121701x + -0.97954669y + 0.69161640 = 0`; VP residual `10.227px`
  - L2: endpoints `(0.959180, 0.748829) -> (0.058104, 0.413722)`; angle `+164.000 deg`; votes `215`; support `351`; span `880.2px`; line `0.34857288x + -0.93728168y + 0.36752002 = 0`; VP residual `19.616px`
  - L3: endpoints `(0.969337, 0.747467) -> (0.104201, 0.467709)`; angle `+166.000 deg`; votes `187`; support `314`; span `837.2px`; line `0.30768192x + -0.95148927y + 0.41295952 = 0`; VP residual `3.531px`
  - L4: endpoints `(0.961670, 0.751335) -> (0.099828, 0.493276)`; angle `+167.000 deg`; votes `201`; support `321`; span `830.6px`; line `0.28684435x + -0.95797720y + 0.44391231 = 0`; VP residual `12.416px`
  - L5: endpoints `(0.985091, 0.595155) -> (0.111821, 0.595155)`; angle `+180.000 deg`; votes `196`; support `253`; span `820.0px`; line `-0.00000000x + -1.00000000y + 0.59515493 = 0`; VP residual `0.035px`
  - L6: endpoints `(0.969700, 0.311015) -> (0.182589, 0.787047)`; angle `-155.000 deg`; votes `190`; support `302`; span `815.5px`; line `-0.51750194x + -0.85568203y + 0.76795171 = 0`; VP residual `6.783px`
  - L7: endpoints `(0.983692, 0.414237) -> (0.156442, 0.721889)`; angle `-164.000 deg`; votes `187`; support `302`; span `808.1px`; line `-0.34857288x + -0.93728168y + 0.73114498 = 0`; VP residual `3.710px`
  - L8: endpoints `(0.985775, 0.321982) -> (0.210530, 0.728215)`; angle `-158.000 deg`; votes `208`; support `333`; span `785.1px`; line `-0.46414382x + -0.88575985y + 0.74273993 = 0`; VP residual `9.366px`
  - L9: endpoints `(0.893259, 0.710822) -> (0.105480, 0.567228)`; angle `+172.000 deg`; votes `187`; support `318`; span `747.0px`; line `0.17932143x + -0.98379054y + 0.53911904 = 0`; VP residual `38.349px`
  - L10: endpoints `(0.870075, 0.553718) -> (0.152290, 0.553718)`; angle `+180.000 deg`; votes `213`; support `259`; span `674.0px`; line `-0.00000000x + -1.00000000y + 0.55371847 = 0`; VP residual `38.915px`

## 3. Double Arch Portico
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_DoubleArch_Rijksmuseum.jpg`
- Crop: `(0.1, 0.14, 0.9, 0.91)`
- Edge pixels used: `80110`
- Hough lines kept: `95`
- Perspective lines used for VP: `10`
- Solved VP: `(0.593908, 0.623095)`
- VP residual mean/max: `27.493px` / `51.959px` on the processing crop
- Perspective measurement lines:
  - L1: endpoints `(0.965546, 0.815964) -> (0.022923, 0.272241)`; angle `+157.000 deg`; votes `337`; support `553`; span `961.6px`; line `0.49965474x + -0.86622465y + 0.22436830 = 0`; VP residual `17.505px`
  - L2: endpoints `(0.962170, 0.816631) -> (0.045012, 0.313083)`; angle `+158.000 deg`; votes `334`; support `551`; span `928.8px`; line `0.48126669x + -0.87657423y + 0.25277718 = 0`; VP residual `7.128px`
  - L3: endpoints `(0.967425, 0.778298) -> (0.052221, 0.350068)`; angle `+161.000 deg`; votes `341`; support `547`; span `908.9px`; line `0.42380766x + -0.90575221y + 0.29494317 = 0`; VP residual `16.660px`
  - L4: endpoints `(0.961683, 0.587722) -> (0.025579, 0.812022)`; angle `-170.000 deg`; votes `335`; support `552`; span `892.6px`; line `-0.23301503x + -0.97247313y + 0.79563008 = 0`; VP residual `48.220px`
  - L5: endpoints `(0.966056, 0.599424) -> (0.031050, 0.732968)`; angle `-174.000 deg`; votes `350`; support `555`; span `882.8px`; line `-0.14139130x + -0.98995379y + 0.72999423 = 0`; VP residual `27.435px`
  - L6: endpoints `(0.960616, 0.586861) -> (0.025529, 0.631234)`; angle `-178.000 deg`; votes `386`; support `610`; span `878.6px`; line `-0.04740050x + -0.99887596y + 0.63173468 = 0`; VP residual `17.682px`
  - L7: endpoints `(0.956526, 0.522818) -> (0.032888, 0.699215)`; angle `-172.000 deg`; votes `324`; support `540`; span `875.8px`; line `-0.18759054x + -0.98224732y + 0.69297188 = 0`; VP residual `28.644px`
  - L8: endpoints `(0.962726, 0.678370) -> (0.033014, 0.678370)`; angle `+180.000 deg`; votes `418`; support `509`; span `873.0px`; line `-0.00000000x + -1.00000000y + 0.67837000 = 0`; VP residual `51.959px`
  - L9: endpoints `(0.940362, 0.594434) -> (0.021299, 0.594434)`; angle `+180.000 deg`; votes `439`; support `619`; span `863.0px`; line `-0.00000000x + -1.00000000y + 0.59443367 = 0`; VP residual `26.941px`
  - L10: endpoints `(0.899319, 0.042507) -> (0.432706, 0.825531)`; angle `-129.000 deg`; votes `332`; support `508`; span `696.2px`; line `-0.85903858x + -0.51191085y + 0.79430946 = 0`; VP residual `32.759px`

## 4. Perspective Street
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Street_NGA_205782.jpg`
- Crop: `(0.01, 0.02, 0.99, 0.96)`
- Edge pixels used: `67467`
- Hough lines kept: `110`
- Perspective lines used for VP: `12`
- Solved VP: `(0.275332, 0.816542)`
- VP residual mean/max: `14.484px` / `33.218px` on the processing crop
- Perspective measurement lines:
  - L1: endpoints `(0.972971, 0.152226) -> (0.119729, 0.969199)`; angle `-143.000 deg`; votes `407`; support `668`; span `1003.2px`; line `-0.69158887x + -0.72229138y + 0.78284704 = 0`; VP residual `2.490px`
  - L2: endpoints `(0.965427, 0.269591) -> (0.066346, 0.956018)`; angle `-149.000 deg`; votes `383`; support `645`; span `984.9px`; line `-0.60683265x + -0.79482963y + 0.80013184 = 0`; VP residual `15.003px`
  - L3: endpoints `(0.881991, 0.042205) -> (0.160478, 0.958984)`; angle `-135.000 deg`; votes `357`; support `560`; span `958.1px`; line `-0.78582441x + -0.61844967y + 0.71919118 = 0`; VP residual `2.032px`
  - L4: endpoints `(0.980563, 0.283624) -> (0.118491, 0.968094)`; angle `-148.000 deg`; votes `346`; support `550`; span `954.5px`; line `-0.62181675x + -0.78316278y + 0.83185492 = 0`; VP residual `19.894px`
  - L5: endpoints `(0.970597, 0.550925) -> (0.027064, 0.963735)`; angle `-161.000 deg`; votes `382`; support `625`; span `937.0px`; line `-0.40083041x + -0.91615227y + 0.89377622 = 0`; VP residual `33.218px`
  - L6: endpoints `(0.825929, 0.075165) -> (0.129443, 0.960145)`; angle `-135.000 deg`; votes `431`; support `698`; span `924.9px`; line `-0.78582441x + -0.61844967y + 0.69552081 = 0`; VP residual `24.282px`
  - L7: endpoints `(0.942513, 0.549473) -> (0.040554, 0.921850)`; angle `-162.000 deg`; votes `364`; support `589`; span `890.5px`; line `-0.38161106x + -0.92432300y + 0.86756342 = 0`; VP residual `7.280px`
  - L8: endpoints `(0.964770, 0.671751) -> (0.040234, 0.836851)`; angle `-172.000 deg`; votes `364`; support `598`; span `876.7px`; line `-0.17579523x + -0.98442676y + 0.83089149 = 0`; VP residual `20.056px`
  - L9: endpoints `(0.972354, 0.790478) -> (0.054360, 0.831211)`; angle `-178.000 deg`; votes `343`; support `547`; span `862.5px`; line `-0.04432797x + -0.99901703y + 0.83280380 = 0`; VP residual `4.568px`
  - L10: endpoints `(0.972354, 0.757982) -> (0.057476, 0.798577)`; angle `-178.000 deg`; votes `349`; support `578`; span `859.6px`; line `-0.04432797x + -0.99901703y + 0.80033963 = 0`; VP residual `25.949px`
  - L11: endpoints `(0.947858, 0.653832) -> (0.079964, 0.888234)`; angle `-168.000 deg`; votes `395`; support `599`; span `833.2px`; line `-0.26073965x + -0.96540915y + 0.87835913 = 0`; VP residual `17.176px`
  - L12: endpoints `(0.966209, 0.659720) -> (0.098211, 0.854193)`; angle `-170.000 deg`; votes `392`; support `587`; span `827.6px`; line `-0.21862735x + -0.97580843y + 0.85500018 = 0`; VP residual `1.865px`

## 5. Interior Hall
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_InteriorHall_MET_DP828125.jpg`
- Crop: `(0.04, 0.05, 0.96, 0.95)`
- Edge pixels used: `71206`
- Hough lines kept: `105`
- Perspective lines used for VP: `12`
- Solved VP: `(0.312831, 0.815337)`
- VP residual mean/max: `15.055px` / `44.358px` on the processing crop
- Perspective measurement lines:
  - L1: endpoints `(0.974356, 0.086358) -> (0.136949, 0.977986)`; angle `-140.000 deg`; votes `251`; support `387`; span `1026.5px`; line `-0.72892293x + -0.68459577y + 0.76935080 = 0`; VP residual `15.844px`
  - L2: endpoints `(0.963515, 0.427592) -> (0.037927, 0.950511)`; angle `-156.000 deg`; votes `245`; support `385`; span `951.4px`; line `-0.49188681x + -0.87065915y + 0.84622724 = 0`; VP residual `16.479px`
  - L3: endpoints `(0.974234, 0.126928) -> (0.224647, 0.953763)`; angle `-139.000 deg`; votes `240`; support `392`; span `932.6px`; line `-0.74086764x + -0.67165105y + 0.80702919 = 0`; VP residual `25.982px`
  - L4: endpoints `(0.971231, 0.544536) -> (0.041410, 0.927898)`; angle `-162.000 deg`; votes `245`; support `387`; span `918.0px`; line `-0.38117034x + -0.92450483y + 0.87363032 = 0`; VP residual `0.569px`
  - L5: endpoints `(0.810885, 0.032893) -> (0.219501, 0.959582)`; angle `-129.000 deg`; votes `238`; support `391`; span `882.4px`; line `-0.84297168x + -0.53795794y + 0.70124817 = 0`; VP residual `1.012px`
  - L6: endpoints `(0.965834, 0.729818) -> (0.033171, 0.833359)`; angle `-175.000 deg`; votes `241`; support `413`; span `879.1px`; line `-0.11033817x + -0.99389410y + 0.83193035 = 0`; VP residual `12.169px`
  - L7: endpoints `(0.952194, 0.758463) -> (0.035107, 0.860274)`; angle `-175.000 deg`; votes `258`; support `427`; span `864.4px`; line `-0.11033817x + -0.99389410y + 0.85889496 = 0`; VP residual `13.178px`
  - L8: endpoints `(0.949933, 0.833398) -> (0.034066, 0.813113)`; angle `+179.000 deg`; votes `274`; support `434`; span `860.1px`; line `0.02214363x + -0.99975480y + 0.81215895 = 0`; VP residual `3.712px`
  - L9: endpoints `(0.942541, 0.859921) -> (0.030997, 0.779038)`; angle `+176.000 deg`; votes `262`; support `420`; span `858.0px`; line `0.08838420x + -0.99608646y + 0.77324954 = 0`; VP residual `10.573px`
  - L10: endpoints `(0.963768, 0.877305) -> (0.073445, 0.758564)`; angle `+174.000 deg`; votes `254`; support `402`; span `840.6px`; line `0.13219822x + -0.99122330y + 0.74219696 = 0`; VP residual `23.151px`
  - L11: endpoints `(0.968301, 0.731736) -> (0.094682, 0.907313)`; angle `-171.000 deg`; votes `246`; support `401`; span `830.6px`; line `-0.19703707x + -0.98039604y + 0.90818195 = 0`; VP residual `44.358px`
  - L12: endpoints `(0.762120, 0.030372) -> (0.238495, 0.912108)`; angle `-127.000 deg`; votes `265`; support `428`; span `817.0px`; line `-0.85981505x + -0.51060560y + 0.67078971 = 0`; VP residual `13.633px`
