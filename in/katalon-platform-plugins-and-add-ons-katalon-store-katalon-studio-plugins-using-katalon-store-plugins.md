---
hide_title: true
title: Using Katalon Store Plugins
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Using <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Store</span>  Plugins

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Plugin is to extend Katalon Studio capabilities and   integrate the software with your favorite tools. This section   introduces plugins, different ways of using plugins with the   Katalon Studio Enterprise license and the detailed   configurations.</p> 

## <a id="id_1" class="anchor_top_offset"/>Introduction to <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Store</span>  Plugins


### <a id="id_2" class="anchor_top_offset"/>Plugins on <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Store</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can find many plugins published on <a className="xref j-external-link" href="https://store.katalon.com/" target="_blank"><span className="ph">Katalon Store</span></a>, which are   developed by the Katalon team or the community user.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Some plugins are exclusive for Katalon Studio Enterprise users   only while the other plugins are available for the community, free   of charge.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can trial an Enterprise plugin for 30 days. After the trial   period, if you wish to continue using the plugin for configuration,   you need to subscribe to a Katalon Studio Enterprise license.</p> 

### <a id="id_3" class="anchor_top_offset"/><span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Store</span>  Plugins usage modes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">All Katalon users are eligible for using the community plugins   published on Store.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Compared to the community users, in addition to Store's plugins,   Katalon Studio Enterprise users can use their private plugins or   all plugins in an offline environment.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Runtime Engine users can use plugins in console   mode.</p> 

### <a id="id_4" class="anchor_top_offset"/><span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Store</span>  Plugin Repository

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio Enterprise users can decide where Katalon Studio   will download plugins for a project. Go to <strong className="ph b">Project &gt;     Settings &gt; Plugins</strong> and select one of the following   options:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <strong className="ph b"><span className="ph">Katalon Store</span> and Local</strong>: Katalon Studio will     install plugins from the <span className="ph">Katalon Store</span> and the Plugins folder of each     project.</li><li className="li">     <strong className="ph b"><span className="ph">Katalon Store</span></strong>: Katalon Studio will install     plugins from <span className="ph">Katalon Store</span> only.</li><li className="li">     <strong className="ph b">Local</strong>: Katalon Studio will install plugins     from the Plugins folder only.</li></ul> 

## <a id="id_9" class="anchor_top_offset"/>Use Plugins in Console Mode

:::tip requirements
- Katalon Studio version 7.0.0 onwards
- An active Katalon Runtime Engine license. To learn more about activating the Katalon Runtime Engine license, you can refer to this document: [Activate Katalon licenses](/katalon-studio/get-started/activate-licenses).
- An API key. To learn more about API keys, you can refer to this document: [Katalon API Key](/katalon-platform/administer/settings/katalon-api-key-in-katalon-testops).
:::
To use plugins from Katalon Store in console mode:

- Install the plugin from Katalon Store.
- While generating commands, use the API Key of the users who have the plugin installed. Both API key command-line options work, either `-apiKey=<Your_API_Key>` or `-apikey=<Your_API_Key>`.

:::info notes
From version 7.7.0 onwards, if you belong to more than one Organization subscribing to Katalon Runtime Engine licenses, you can choose which Organization validates your license usage with the following command line: `-orgID=<Katalon_OrgID>`.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you use the private plugins, make sure you store all plugins in the <code className="ph codeph">&lt;project_name&gt;/Plugins</code> folder. See above: <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/private-plugins-in-katalon-studio">Private Plugins</a>.</p> 
