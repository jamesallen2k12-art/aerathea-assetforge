# P08 Formula-Applied Perspective Redraw Measurements

P08 applies the researched formulas directly: Sobel gradients, Canny-style non-maximum suppression, gradient-guided Hough voting, homogeneous line equations, and weighted least-squares vanishing-point solving.

## 1. Arcade Capriccio
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Arcade_Capriccio_MET_DP836399.jpg`
- Work size: `760 x 516`
- Non-maximum-suppressed edge points: `13156`
- Hough lines kept: `85`
- Weighted least-squares VP: `(0.817001, 0.869941)`
- VP residual mean/max: `2.234px` / `5.526px`
- Perspective inliers:
  - L1: endpoints `(0.799004, 0.722521) -> (0.719975, 0.061978)`; angle `+100.000 deg`; equation `0.99291881x + -0.11879495y + -0.70751393 = 0`; support `66`; span `345.4px`; weight `3488.8`; residual `0.271px`
  - L2: endpoints `(0.763866, 0.609843) -> (0.646165, 0.042458)`; angle `+107.000 deg`; equation `0.97915360x + -0.20312122y + -0.62407058 = 0`; support `50`; span `305.6px`; weight `2545.4`; residual `0.612px`
  - L3: endpoints `(0.936307, 0.950662) -> (0.016992, 0.318875)`; angle `+155.000 deg`; equation `0.56638213x + -0.82414276y + 0.25317402 = 0`; support `49`; span `769.9px`; weight `5133.2`; residual `0.796px`
  - L4: endpoints `(0.955149, 0.840194) -> (0.193844, 0.997881)`; angle `-172.000 deg`; equation `-0.20282216x + -0.97921559y + 1.01645660 = 0`; support `36`; span `583.5px`; weight `3638.8`; residual `0.843px`
  - L5: endpoints `(0.865631, 0.860455) -> (0.203036, 0.963092)`; angle `-174.000 deg`; equation `-0.15307560x + -0.98821448y + 0.98282147 = 0`; support `35`; span `505.7px`; weight `2685.1`; residual `1.467px`
  - L6: endpoints `(0.865579, 0.859483) -> (0.189861, 0.929120)`; angle `-176.000 deg`; equation `-0.10251423x + -0.99473154y + 0.94368885 = 0`; support `61`; span `514.1px`; weight `4687.6`; residual `4.122px`
  - L7: endpoints `(0.963129, 0.883158) -> (0.151523, 0.778510)`; angle `+175.000 deg`; equation `0.12788095x + -0.99178953y + 0.75274135 = 0`; support `69`; span `618.4px`; weight `6761.5`; residual `4.239px`
  - L8: endpoints `(0.853737, 0.863612) -> (0.013138, 0.841988)`; angle `+179.000 deg`; equation `0.02571653x + -0.99966928y + 0.84137148 = 0`; support `58`; span `638.1px`; weight `5397.4`; residual `5.526px`

## 2. Palace Fantasy
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Palace_Fantasy_NationalTrust.jpg`
- Work size: `760 x 586`
- Non-maximum-suppressed edge points: `14004`
- Hough lines kept: `85`
- Weighted least-squares VP: `(0.502573, 0.739251)`
- VP residual mean/max: `7.593px` / `16.273px`
- Perspective inliers:
  - L1: endpoints `(0.489528, 0.700462) -> (0.350612, 0.361489)`; angle `+118.000 deg`; equation `0.92531179x + -0.37920718y + -0.18734599 = 0`; support `35`; span `224.6px`; weight `3756.8`; residual `2.005px`
  - L2: endpoints `(0.642951, 0.742418) -> (0.259552, 0.742418)`; angle `+180.000 deg`; equation `-0.00000000x + -1.00000000y + 0.74241818 = 0`; support `74`; span `291.0px`; weight `8531.4`; residual `2.407px`
  - L3: endpoints `(0.870799, 0.701319) -> (0.388816, 0.756029)`; angle `-175.000 deg`; equation `-0.11278665x + -0.99361923y + 0.79505824 = 0`; support `81`; span `367.2px`; weight `10520.4`; residual `2.919px`
  - L4: endpoints `(0.993434, 0.799678) -> (0.108035, 0.699176)`; angle `+175.000 deg`; equation `0.11278665x + -0.99361923y + 0.68252940 = 0`; support `83`; span `674.6px`; weight `20252.3`; residual `3.556px`
  - L5: endpoints `(0.993304, 0.538027) -> (0.417155, 0.780910)`; angle `-162.000 deg`; equation `-0.38845602x + -0.92146726y + 0.88162952 = 0`; support `38`; span `459.8px`; weight `6173.6`; residual `3.957px`
  - L6: endpoints `(0.994760, 0.799685) -> (0.357306, 0.698135)`; angle `+173.000 deg`; equation `0.15732134x + -0.98754746y + 0.63323004 = 0`; support `51`; span `487.5px`; weight `7324.2`; residual `13.490px`
  - L7: endpoints `(0.994692, 0.521206) -> (0.247048, 0.817771)`; angle `-163.000 deg`; equation `-0.36871748x + -0.92954151y + 0.85124264 = 0`; support `43`; span `593.4px`; weight `7819.2`; residual `16.134px`
  - L8: endpoints `(0.869556, 0.702470) -> (0.362513, 0.783244)`; angle `-173.000 deg`; equation `-0.15732134x + -0.98754746y + 0.83052200 = 0`; support `47`; span `387.7px`; weight `7233.6`; residual `16.273px`

## 3. Double Arch Portico
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_DoubleArch_Rijksmuseum.jpg`
- Work size: `760 x 559`
- Non-maximum-suppressed edge points: `14927`
- Hough lines kept: `85`
- Weighted least-squares VP: `(0.671318, 0.189275)`
- VP residual mean/max: `7.827px` / `14.057px`
- Perspective inliers:
  - L1: endpoints `(0.828671, 0.217336) -> (0.032685, 0.065171)`; angle `+172.000 deg`; equation `0.18776566x + -0.98221386y + 0.05787481 = 0`; support `120`; span `610.1px`; weight `28044.4`; residual `1.507px`
  - L2: endpoints `(0.828742, 0.211164) -> (0.332034, 0.152054)`; angle `+175.000 deg`; equation `0.11816959x + -0.99299343y + 0.11175255 = 0`; support `138`; span `378.4px`; weight `19315.2`; residual `2.381px`
  - L3: endpoints `(0.756258, 0.198134) -> (0.201581, 0.198134)`; angle `+180.000 deg`; equation `-0.00000000x + -1.00000000y + 0.19813433 = 0`; support `337`; span `421.0px`; weight `66245.5`; residual `6.733px`
  - L4: endpoints `(0.714074, 0.179271) -> (0.338602, 0.170356)`; angle `+179.000 deg`; equation `0.02373595x + -0.99971826y + 0.16227103 = 0`; support `291`; span `285.0px`; weight `34925.4`; residual `8.372px`
  - L5: endpoints `(0.906617, 0.174127) -> (0.350260, 0.253666)`; angle `-174.000 deg`; equation `-0.14152537x + -0.98993463y + 0.30068364 = 0`; support `51`; span `424.6px`; weight `8464.6`; residual `13.912px`
  - L6: endpoints `(0.715498, 0.166493) -> (0.221264, 0.213502)`; angle `-176.000 deg`; equation `-0.09468815x + -0.99550698y + 0.23349415 = 0`; support `134`; span `376.0px`; weight `19613.8`; residual `14.057px`

## 4. Perspective Street
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_Street_NGA_205782.jpg`
- Work size: `760 x 598`
- Non-maximum-suppressed edge points: `14220`
- Hough lines kept: `85`
- Weighted least-squares VP: `(0.161880, 0.841649)`
- VP residual mean/max: `7.758px` / `13.244px`
- Perspective inliers:
  - L1: endpoints `(0.731324, 0.980927) -> (0.323203, 0.880069)`; angle `+169.000 deg`; equation `0.23990946x + -0.97079527y + 0.77682738 = 0`; support `122`; span `315.6px`; weight `13416.1`; residual `1.068px`
  - L2: endpoints `(0.160139, 0.809235) -> (0.032354, 0.157639)`; angle `+104.000 deg`; equation `0.98130758x + -0.19244595y + -0.00141171 = 0`; support `58`; span `400.9px`; weight `9203.4`; residual `3.443px`
  - L3: endpoints `(0.808979, 0.298196) -> (0.279723, 0.752055)`; angle `-146.000 deg`; equation `-0.65096558x + -0.75910725y + 0.75298009 = 0`; support `25`; span `484.5px`; weight `4678.0`; residual `6.612px`
  - L4: endpoints `(0.108283, 0.461889) -> (0.054349, 0.139295)`; angle `+102.000 deg`; equation `0.98631029x + -0.16489999y + -0.03063490 = 0`; support `208`; span `196.9px`; weight `17570.8`; residual `7.417px`
  - L5: endpoints `(0.699652, 0.771206) -> (0.263662, 0.819700)`; angle `-175.000 deg`; equation `-0.11054756x + -0.99387083y + 0.84382353 = 0`; support `64`; span `332.2px`; weight `6476.7`; residual `8.028px`
  - L6: endpoints `(0.774887, 0.689540) -> (0.303507, 0.816923)`; angle `-168.000 deg`; equation `-0.26087750x + -0.96537191y + 0.86781279 = 0`; support `142`; span `365.8px`; weight `20573.6`; residual `9.939px`
  - L7: endpoints `(0.809031, 0.102282) -> (0.297266, 0.667871)`; angle `-139.000 deg`; equation `-0.74150873x + -0.67094322y + 0.66852923 = 0`; support `65`; span `514.7px`; weight `11345.2`; residual `12.316px`
  - L8: endpoints `(0.928700, 0.996365) -> (0.346195, 0.892285)`; angle `+172.000 deg`; equation `0.17589187x + -0.98440949y + 0.81748084 = 0`; support `144`; span `446.5px`; weight `22795.2`; residual `13.244px`

## 5. Interior Hall
- Source file: `SourceAssets/Reference/PerspectiveDrawing/WebReferences/REF_Perspective_InteriorHall_MET_DP828125.jpg`
- Work size: `760 x 599`
- Non-maximum-suppressed edge points: `14915`
- Hough lines kept: `85`
- Weighted least-squares VP: `(0.665902, 0.938100)`
- VP residual mean/max: `7.247px` / `16.951px`
- Perspective inliers:
  - L1: endpoints `(0.763991, 0.965831) -> (0.049642, 0.756509)`; angle `+167.000 deg`; equation `0.28120112x + -0.95964886y + 0.71202365 = 0`; support `82`; span `556.5px`; weight `14564.2`; residual `0.738px`
  - L2: endpoints `(0.758905, 0.942936) -> (0.164751, 0.890203)`; angle `+176.000 deg`; equation `0.08840575x + -0.99608455y + 0.87215249 = 0`; support `75`; span `452.1px`; weight `11244.6`; residual `2.588px`
  - L3: endpoints `(0.587760, 0.613660) -> (0.477317, 0.124802)`; angle `+106.000 deg`; equation `0.97541707x + -0.22036682y + -0.43808100 = 0`; support `65`; span `304.1px`; weight `9556.5`; residual `3.591px`
  - L4: endpoints `(0.961811, 0.938374) -> (0.143649, 0.920248)`; angle `+179.000 deg`; equation `0.02214907x + -0.99975468y + 0.91684087 = 0`; support `224`; span `621.1px`; weight `44400.7`; residual `4.773px`
  - L5: endpoints `(0.734943, 0.935947) -> (0.258143, 0.872341)`; angle `+174.000 deg`; equation `0.13223014x + -0.99121904y + 0.83054666 = 0`; support `89`; span `363.9px`; weight `10876.1`; residual `8.561px`
  - L6: endpoints `(0.695356, 0.967442) -> (0.343093, 0.777658)`; angle `+157.000 deg`; equation `0.47430112x + -0.88036268y + 0.52189185 = 0`; support `78`; span `290.5px`; weight `7343.9`; residual `9.015px`
  - L7: endpoints `(0.764340, 0.964230) -> (0.314056, 0.767442)`; angle `+161.000 deg`; equation `0.40045825x + -0.91631501y + 0.57745215 = 0`; support `78`; span `361.5px`; weight `8974.2`; residual `11.763px`
  - L8: endpoints `(0.703557, 0.960404) -> (0.056653, 0.960404)`; angle `+180.000 deg`; equation `0.00000000x + -1.00000000y + 0.96040443 = 0`; support `146`; span `491.0px`; weight `22083.3`; residual `16.951px`
