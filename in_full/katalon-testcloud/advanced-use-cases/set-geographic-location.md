---
title: Set geographic location
---

:::caution Requirements
- You have installed the Katalon TestCloud Keywords plugin to automatically load all TestCloud keywords into your project without having to manually define them. If you have not, visit Katalon Store: [Katalon TestCloud keywords](https://store.katalon.com/product/397/Katalon-TestCloud-Keywords).
- This keyword is applicable for desktop browser testing (Windows, macOS), mobile browser testing, and mobile native app testing.
:::

TestCloud supports setting geographic location for mobile and web testing. In some test scenarios, you may want to dynamically set geographic location (or geolocation) to:

- Ensure the website and mobile app display correctly when accessed from different geolocations.
- Verify that localization features such as language translation, currency change, and time zone changes reflect accurately according to different locations.
- Confirm that blocked or restricted content like images, content, or videos are blocked as intended from different locations.

You can simulate geolocation at the start of testing sessions using the desired capability `geoLocation`.

1. In Katalon Studio, click the **Profile** drop-down and select **Reload Plugins** to make sure the plugin is installed.
    
<img width="500" alt="Reload plugins" src="https://docs.katalon.com/3a871180-56d3-4a86-aa06-9441c30937e4/KS_TestCloud_plugin.png" />
    
2. Go to **Project Settings** > **Desired Capabilities** > **TestCloud**.
3. In the TestCloud table, add a `katalon:options` property, set **Type** as `Dictionary`, then click the `...`.
    
<img width="600" alt="TestCloud desired capabilities settings" src="https://docs.katalon.com/3d76cb0e-d7e8-4c16-8323-869daa78a0ac/KS_TestCloud_desired_caps_menu.png" />
    
4. In the **Dictionary Property Builder** dialog, add the String property `geoLocation=<country-code>`. Then, click **OK**.
    
<img width="600" alt="Dictionary Property Builder dialog" src="https://docs.katalon.com/58ceff82-a6c8-4079-a0d1-2a50e42c1fcd/KS_TestCloud_geo_location.png" />
    
5. Add the `setMobileGeoLocation` keyword to your test case as needed.
    
    <img width="600" alt="Add keyword to test case" src="https://docs.katalon.com/417c9667-990d-4ce2-956c-7f873aebee6f/add-testcloud-custom-keyword.png" />
    
6. Configure your TestCloud environment and run the test.

:::info
- Geolocation testing cannot be performed together with private/local testing using TestCloud Tunnel or by whitelisting TestCloud IPs. 
- If you need to test both geolocation and private/local environments, we recommend leveraging parallel testing - run two separate tests simultaneously: one for geolocation and another for private/local testing.
:::

## Supported IP Geolocations
The following is the list of supported IP Geolocations.

| **Country** | **Code** |
| ----------- | -------- |
| Adelaide (Australia) | AU/AL |
| Albania | AL |
| Alberta (Canada) | CA/AB |
| Albuquerque, New Mexico (US) | US/ABQ |
| Andorra | AD |
| Andhra Pradesh (India) | IN/AP |
| Ankara (Turkey) | TR/ANK |
| Argentina | AR |
| Armenia | AM |
| Ashburn, Virginia (US) | US/AB |
| Atlanta, Georgia (US) | US/AT |
| Auckland (New Zealand) | NZ/AU |
| Australia	| AU |
| Austria | AT |
| Azerbaijan | AZ |
| Bahrain | BH |
| Bangladesh | BD |
| Barcelona (Spain) | ES/BCN |
| Belarus | BY |
| Belgium | BE |
| Berlin | V2 |
| Berkeley Springs, WV (US)	| US/BS |
| Billings, Montana (US) | US/BL |
| Boca Raton, Florida (US)	| US/BR |
| Bolivia (La Paz) | BO/LPZ |
| Bosnia and Herzegovina | BA |
| Boston, Massachusetts (US) | US/BO |
| Brazil | BR |
| British Colombia (Canada)	| CA/BC |
| Brunswick, Maine (US)	| US/BWK |
| Buffalo, New York (US) | US/BU |
| Bulgaria	| BG |
| Cambodia	| KH |
| Canada | CA |
| Canberra (Australia) | AU/CN |
| Charlotte, NC (US) | US/CH |
| Cheyenne, Wyoming (US) | US/CY |
| Chile | CL |
| China | CN |
| Chicago, Illinois (US) | US/CHI |
| Colombia | CO |
| Columbus, Ohio (US) | US/CO |
| Connecticut (US) | US/CN |
| Costa Rica | CR |
| Cromwell, Connecticut (US) | US/CM |
| Curacao | CW |
| Cyprus | CY |
| Czech Republic | CZ |
| Dallas, Texas (US) | US/DL |
| Dallas-Ft. Worth, Texas (US) | US/DFW |
| Denmark | DK |
| Denver, Colorado (US) | Y6 |
| Des Moines, Iowa (US) | US/DM |
| Detroit, Michigan (US) | US/DET |
| Dominican Republic | DO |
| Dublin (Ireland) | IE/DU |
| Ecuador | EC |
| Egypt | EG |
| El Salvador | SV |
| Estonia | EE |
| Finland | FI |
| France | FR |
| Georgia | GE |
| Germany | DE |
| Greece | GR |
| Guatemala | GT |
| Harrisburg, Pennsylvania (US) | US/HB |
| Hollywood, Florida (US) | US/HW |
| Honduras | HN |
| Hong Kong | HK |
| Honolulu, HI | U3 |
| Houston, Texas (US) | US/HO |
| Hungary | HU |
| Iceland | IS |
| India | IN |
| Indonesia | ID |
| Indianapolis, Indiana (US) | US/IN |
| Iowa (US) | US/IW |
| Ireland | IE |
| Isle of Man | IM |
| Israel | IL |
| Italy | IT |
| Jamaica | JM |
| Japan | JP |
| Jersey City, New Jersey (US) | US/JC |
| Jordan | JO |
| Kansas City, Missouri (US) | US/KC |
| Kazakhstan | KZ |
| Kenya | KE |
| Korea | KR |
| Kuwait | KW |
| Kyrgyzstan | KG |
| La Paz (Bolivia) | BO/LPZ |
| Las Vegas, Nevada (US) | US/LV |
| Latvia | LV |
| Lebanon | LB |
| Lincoln, Nebraska (US) | US/LC |
| Lithuania | LT |
| London | W8 |
| Los Angeles, California (US) | US/LA |
| Luxembourg | LU |
| Madrid (Spain) | ES/MAD |
| Manhattan, New York (US) | US/MHT |
| Maryland (US) | US/ML |
| Malta | MT |
| Melbourne (Australia) | AU/ML |
| Memphis, Tennessee (US) | W4 |
| Mexico | MX |
| Miami, Florida (US) | US/MI |
| Milan (Italy) | IT/MIL |
| Minneapolis, Minnesota (US) | US/MIN |
| Minnesota (US) | US/MN |
| Moldova | MD |
| Mongolia | MN |
| Montana (US) | US/MT |
| Monticello, Illinois (US) | US/MO |
| Morocco | MA |
| Mumbai (India) | IN/MU |
| Munich (Germany) | DE/MUN |
| Nairobi (Kenya) | KE/NAI |
| Nebraska (US) | US/NB |
| New Hamisphere (US) | US/NH |
| New Jersey, New Jersey | X4 |
| New Orleans, Louisiana (US) | US/NO |
| New York City, New York (US) | US/NYC |
| New York City, New York (US) | Z0 |
| New Zealand | NZ |
| Nicaragua | NI |
| Nigeria | NG |
| Norway | NO |
| Oklahoma City, Oklahoma (US) | US/OKC |
| Oman | OM |
| Ontario (Canada) | CA/ON |
| Orlando, Florida (US) | US/ORL |
| Pakistan | PK |
| Panama | PA |
| Paraguay | PY |
| Paris (France) | FR/PA |
| Perth (Australia) | AU/PT |
| Peru | PE |
| Philippines | PH |
| Phoenix, Arizona (US) | US/PHX |
| Pittsburgh, Pennsylvania (US) | US/PIT |
| Poland | PL |
| Portugal | PT |
| Puerto Rico | PR |
| Qatar | QA |
| Raleigh, North Carolina (US) | US/RA |
| Reston, Virginia (US) | US/RT |
| Reykjavik (Iceland) | IS/REK |
| Richmond, Virginia (US) | US/RM |
| Romania | RO |
| Russian Federation | RU |
| Sacramento, California (US) | US/SAC |
| Saint Petersburg (Russia) | RU/SP |
| Salem, New Hampshire (US) | US/SLE |
| Salem, NH | U5 |
| Salt Lake City, Utah (US) | US/SLC |
| San Diego, California (US) | US/SD |
| San Francisco, California (US) | US/SF |
| San Jose, California (US) | US/SJ |
| Santa Clara, California (US) | US/SC |
| Saudi Arabia | SA |
| Serbia | RS |
| Seattle, Washington (US) | US/SEA |
| Singapore | SG |
| Sioux Falls, South Dakota (US) | US/SFL |
| Slovakia | SK |
| Slovenia | SI |
| South Africa | ZA |
| South Bend, Indiana (US) | US/SB |
| Spain | ES |
| Sterling, Virginia (US) | US/ST |
| St Louis, Missouri (US) | US/STL |
| Sweden | SE |
| Switzerland | CH |
| Sydney (Australia) | AU/SY |
| Taiwan | TW |
| Tampa, Florida (US) | US/TPA |
| Tanzania | TZ |
| Thailand | TH |
| Tunisia | TN |
| Turkey | TR |
| Turkmenistan | TM |
| Ukraine | UA |
| United Arab Emirates | AE |
| United Kingdom | GB |
| United States | US |
| Uruguay | UY |
| Uzbekistan | UZ |
| Venezuela | VE |
| Vietnam | VN |
| Washington | Z6 |
| Washington (Herndon), Virginia | US/WAV |
| Wilmington, DE | U4 |
| Wilmington, Delaware (US) | US/WILM |