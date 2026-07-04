# P06 Measured Vector Perspective Redraw Data

P06 applies the lesson from P05: keep source-pixel measurement, but remove paper grain and texture by redrawing only classified Hough line spans.
Perspective lines, verticals, horizontals, and secondary diagonals are all detected from the downloaded image pixels.
For each perspective line: `ax + by + c = 0`; the vanishing point is the least-squares intersection of selected red lines.

## 1. Arcade Capriccio
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Arcade_Capriccio_MET_DP836399.jpg`
- Solved VP: `(0.461698, 0.553743)`
- VP residual mean/max: `18.641px` / `32.259px`
- Displayed lines: `7` perspective, `5` vertical, `12` horizontal, `8` secondary diagonal
- Perspective measurement lines:
  - L1: endpoints `(0.871545, 0.095891) -> (0.154730, 0.890889)`; angle `-143.000 deg`; equation `-0.74268244x + -0.66964378y + 0.71149379 = 0`; votes `257`; support `413`; span `842.8px`; residual `2.080px`
  - L2: endpoints `(0.824628, 0.966871) -> (0.051430, 0.077782)`; angle `+142.000 deg`; equation `0.75457328x + -0.65621579y + 0.01223408 = 0`; votes `224`; support `353`; span `921.3px`; residual `2.591px`
  - L3: endpoints `(0.820693, 0.967854) -> (0.042471, 0.104751)`; angle `+143.000 deg`; equation `0.74268244x + -0.66964378y + 0.03860312 = 0`; votes `219`; support `338`; span `915.0px`; residual `10.046px`
  - L4: endpoints `(0.795908, 0.067886) -> (0.137879, 0.971007)`; angle `-137.000 deg`; equation `-0.80821902x + -0.58888201y + 0.68324539 = 0`; votes `253`; support `419`; span `844.9px`; residual `15.038px`
  - L5: endpoints `(0.811703, 0.946285) -> (0.071590, 0.183557)`; angle `+145.000 deg`; equation `0.71766622x + -0.69638725y + 0.07644920 = 0`; votes `241`; support `360`; span `848.4px`; residual `20.844px`
  - L6: endpoints `(0.953894, 0.830491) -> (0.021817, 0.358137)`; angle `+161.000 deg`; equation `0.45204300x + -0.89199615y + 0.30959423 = 0`; votes `226`; support `371`; span `925.7px`; residual `22.903px`
  - L7: endpoints `(0.948378, 0.052997) -> (0.116996, 0.847623)`; angle `-147.000 deg`; equation `-0.69094619x + -0.72290620y + 0.69359007 = 0`; votes `268`; support `431`; span `930.8px`; residual `24.180px`

## 2. Palace Fantasy
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Palace_Fantasy_NationalTrust.jpg`
- Solved VP: `(0.485996, 0.595118)`
- VP residual mean/max: `14.295px` / `38.915px`
- Displayed lines: `7` perspective, `12` vertical, `11` horizontal, `8` secondary diagonal
- Perspective measurement lines:
  - L1: endpoints `(0.985091, 0.595155) -> (0.111821, 0.595155)`; angle `+180.000 deg`; equation `-0.00000000x + -1.00000000y + 0.59515493 = 0`; votes `196`; support `253`; span `820.0px`; residual `0.035px`
  - L2: endpoints `(0.969337, 0.747467) -> (0.104201, 0.467709)`; angle `+166.000 deg`; equation `0.30768192x + -0.95148927y + 0.41295952 = 0`; votes `187`; support `314`; span `837.2px`; residual `3.531px`
  - L3: endpoints `(0.983692, 0.414237) -> (0.156442, 0.721889)`; angle `-164.000 deg`; equation `-0.34857288x + -0.93728168y + 0.73114498 = 0`; votes `187`; support `302`; span `808.1px`; residual `3.710px`
  - L4: endpoints `(0.969700, 0.311015) -> (0.182589, 0.787047)`; angle `-155.000 deg`; equation `-0.51750194x + -0.85568203y + 0.76795171 = 0`; votes `190`; support `302`; span `815.5px`; residual `6.783px`
  - L5: endpoints `(0.985775, 0.321982) -> (0.210530, 0.728215)`; angle `-158.000 deg`; equation `-0.46414382x + -0.88575985y + 0.74273993 = 0`; votes `208`; support `333`; span `785.1px`; residual `9.366px`
  - L6: endpoints `(0.973281, 0.506128) -> (0.043777, 0.697065)`; angle `-171.000 deg`; equation `-0.20121701x + -0.97954669y + 0.69161640 = 0`; votes `196`; support `312`; span `883.7px`; residual `10.227px`
  - L7: endpoints `(0.961670, 0.751335) -> (0.099828, 0.493276)`; angle `+167.000 deg`; equation `0.28684435x + -0.95797720y + 0.44391231 = 0`; votes `201`; support `321`; span `830.6px`; residual `12.416px`

## 3. Double Arch Portico
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_DoubleArch_Rijksmuseum.jpg`
- Solved VP: `(0.593908, 0.623095)`
- VP residual mean/max: `27.493px` / `51.959px`
- Displayed lines: `7` perspective, `6` vertical, `12` horizontal, `8` secondary diagonal
- Perspective measurement lines:
  - L1: endpoints `(0.962170, 0.816631) -> (0.045012, 0.313083)`; angle `+158.000 deg`; equation `0.48126669x + -0.87657423y + 0.25277718 = 0`; votes `334`; support `551`; span `928.8px`; residual `7.128px`
  - L2: endpoints `(0.967425, 0.778298) -> (0.052221, 0.350068)`; angle `+161.000 deg`; equation `0.42380766x + -0.90575221y + 0.29494317 = 0`; votes `341`; support `547`; span `908.9px`; residual `16.660px`
  - L3: endpoints `(0.965546, 0.815964) -> (0.022923, 0.272241)`; angle `+157.000 deg`; equation `0.49965474x + -0.86622465y + 0.22436830 = 0`; votes `337`; support `553`; span `961.6px`; residual `17.505px`
  - L4: endpoints `(0.960616, 0.586861) -> (0.025529, 0.631234)`; angle `-178.000 deg`; equation `-0.04740050x + -0.99887596y + 0.63173468 = 0`; votes `386`; support `610`; span `878.6px`; residual `17.682px`
  - L5: endpoints `(0.940362, 0.594434) -> (0.021299, 0.594434)`; angle `+180.000 deg`; equation `-0.00000000x + -1.00000000y + 0.59443367 = 0`; votes `439`; support `619`; span `863.0px`; residual `26.941px`
  - L6: endpoints `(0.966056, 0.599424) -> (0.031050, 0.732968)`; angle `-174.000 deg`; equation `-0.14139130x + -0.98995379y + 0.72999423 = 0`; votes `350`; support `555`; span `882.8px`; residual `27.435px`
  - L7: endpoints `(0.956526, 0.522818) -> (0.032888, 0.699215)`; angle `-172.000 deg`; equation `-0.18759054x + -0.98224732y + 0.69297188 = 0`; votes `324`; support `540`; span `875.8px`; residual `28.644px`

## 4. Perspective Street
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Street_NGA_205782.jpg`
- Solved VP: `(0.275332, 0.816542)`
- VP residual mean/max: `14.484px` / `33.218px`
- Displayed lines: `7` perspective, `12` vertical, `9` horizontal, `8` secondary diagonal
- Perspective measurement lines:
  - L1: endpoints `(0.966209, 0.659720) -> (0.098211, 0.854193)`; angle `-170.000 deg`; equation `-0.21862735x + -0.97580843y + 0.85500018 = 0`; votes `392`; support `587`; span `827.6px`; residual `1.865px`
  - L2: endpoints `(0.881991, 0.042205) -> (0.160478, 0.958984)`; angle `-135.000 deg`; equation `-0.78582441x + -0.61844967y + 0.71919118 = 0`; votes `357`; support `560`; span `958.1px`; residual `2.032px`
  - L3: endpoints `(0.972971, 0.152226) -> (0.119729, 0.969199)`; angle `-143.000 deg`; equation `-0.69158887x + -0.72229138y + 0.78284704 = 0`; votes `407`; support `668`; span `1003.2px`; residual `2.490px`
  - L4: endpoints `(0.972354, 0.790478) -> (0.054360, 0.831211)`; angle `-178.000 deg`; equation `-0.04432797x + -0.99901703y + 0.83280380 = 0`; votes `343`; support `547`; span `862.5px`; residual `4.568px`
  - L5: endpoints `(0.942513, 0.549473) -> (0.040554, 0.921850)`; angle `-162.000 deg`; equation `-0.38161106x + -0.92432300y + 0.86756342 = 0`; votes `364`; support `589`; span `890.5px`; residual `7.280px`
  - L6: endpoints `(0.965427, 0.269591) -> (0.066346, 0.956018)`; angle `-149.000 deg`; equation `-0.60683265x + -0.79482963y + 0.80013184 = 0`; votes `383`; support `645`; span `984.9px`; residual `15.003px`
  - L7: endpoints `(0.947858, 0.653832) -> (0.079964, 0.888234)`; angle `-168.000 deg`; equation `-0.26073965x + -0.96540915y + 0.87835913 = 0`; votes `395`; support `599`; span `833.2px`; residual `17.176px`

## 5. Interior Hall
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_InteriorHall_MET_DP828125.jpg`
- Solved VP: `(0.312831, 0.815337)`
- VP residual mean/max: `15.055px` / `44.358px`
- Displayed lines: `7` perspective, `11` vertical, `7` horizontal, `8` secondary diagonal
- Perspective measurement lines:
  - L1: endpoints `(0.971231, 0.544536) -> (0.041410, 0.927898)`; angle `-162.000 deg`; equation `-0.38117034x + -0.92450483y + 0.87363032 = 0`; votes `245`; support `387`; span `918.0px`; residual `0.569px`
  - L2: endpoints `(0.810885, 0.032893) -> (0.219501, 0.959582)`; angle `-129.000 deg`; equation `-0.84297168x + -0.53795794y + 0.70124817 = 0`; votes `238`; support `391`; span `882.4px`; residual `1.012px`
  - L3: endpoints `(0.949933, 0.833398) -> (0.034066, 0.813113)`; angle `+179.000 deg`; equation `0.02214363x + -0.99975480y + 0.81215895 = 0`; votes `274`; support `434`; span `860.1px`; residual `3.712px`
  - L4: endpoints `(0.942541, 0.859921) -> (0.030997, 0.779038)`; angle `+176.000 deg`; equation `0.08838420x + -0.99608646y + 0.77324954 = 0`; votes `262`; support `420`; span `858.0px`; residual `10.573px`
  - L5: endpoints `(0.965834, 0.729818) -> (0.033171, 0.833359)`; angle `-175.000 deg`; equation `-0.11033817x + -0.99389410y + 0.83193035 = 0`; votes `241`; support `413`; span `879.1px`; residual `12.169px`
  - L6: endpoints `(0.952194, 0.758463) -> (0.035107, 0.860274)`; angle `-175.000 deg`; equation `-0.11033817x + -0.99389410y + 0.85889496 = 0`; votes `258`; support `427`; span `864.4px`; residual `13.178px`
  - L7: endpoints `(0.762120, 0.030372) -> (0.238495, 0.912108)`; angle `-127.000 deg`; equation `-0.85981505x + -0.51060560y + 0.67078971 = 0`; votes `265`; support `428`; span `817.0px`; residual `13.633px`
