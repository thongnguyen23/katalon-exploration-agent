---
title: Use TestOps Visual Testing
---
import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel, MarjNote_Value } from "../../../../reusable-component";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import useBaseUrl from '@docusaurus/useBaseUrl';

You can compare images captured during test executions with [TestOps Visual Testing](https://docs.katalon.com/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview#id_3).


<Tabs>
  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

## Set up a new baseline

You can set up a new baseline image to compare it with the screenshot of the next Test Run:

:::info notes
If you run a Test Suite for the first time and the Test Suite has passed, the screenshots are automatically marked as **Passed** and there is no **Save to baseline** button. You can open a screenshot and click **Failed**, then switch back to **Passed** so that the **Save to baseline** button appears.
:::

1. Navigate to your **specific project's UI > Executions**. Select the test suite that has Visual Testing.
<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/executions-list.png" alt="List of available test suite in Executions" width="600"/>

2. Click the `Visual Testing` tab. Then, select a checkpoint you need to configure.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/visual-testing-tab.png" alt="Click on visual testing tab" width="700"/>


3. Click **Mark as Passed.**
4. Then, click **Save to baseline**.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/no-baseline-save.png" alt="Save a checkpoint to baseline" width="800"/>


## Unresolved images

If you run the Test Suite again and the new screenshots from this test execution differ from the baseline images, the status of this Visual Test Run is marked as **Unresolved**. To resolve these images:


1. Navigate to your **specific project's UI > Executions**. Select the test suite containing the Visual Testing results you need to resolve.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/executions-list.png" alt="List of available test suite in Executions" width="600"/>

2. Click the **Visual Testing** tab, then select an **Unresolved** checkpoint.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/visual-testing-tab.png" alt="Click on visual testing tab" width="700"/>

- If there is only a Baseline and no Checkpoint, it means the test suite did not capture a screenshot for that checkpoint.

- If there is a Checkpoint and no Baseline, it means the test suite captured a screenshot, but there is no baseline to compare it to. You can make that Checkpoint the new Baseline.

- If there is a mismatch, it means the screenshot captured differ from the baseline, you need to compare the images:

    - Select one of the three comparison options to compare the new screenshot (on the right) with the baseline image (on the left).
    The Comparison Method is **enabled only** if the screenshot status is **Mismatch**.

        - **Pixel**: This method compares the pixel resolution of two images to figure out the pixel-by-pixel differences between them. See: [Pixel-based comparison](/katalon-platform/analyze/visual-testing/visual-testing-overview#pixel-based-comparison).
        - **Layout**: This method identifies and maps the similar zones between the baseline and checkpoint images, highlighting the layout differences between the two images. See: [Layout-based comparison](/katalon-platform/analyze/visual-testing/visual-testing-overview#layout-based-comparison).
        - **Text Content**: This method identifies the text content differences between two images. See: [Content-based comparison](/katalon-platform/analyze/visual-testing/visual-testing-overview#content-based-comparison).

        <img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/mismatch-dropdown.png" alt="Compare method" width="700"/>


3. Click **Mark as Passed** or **Mark as Failed** to resolve the checkpoint.


## Ignored zones

Specifying ignored zones is especially useful when testing a website with dynamic content, such as pop-up ads, that changes between runs. By defining ignored zones, Visual Testing will skip these areas when comparing captured screenshots to their baselines.

### Add an ignored zone to a single baseline image

To configure an ignored zone, follow these steps:

1. In your project’s UI, navigate to **Assets > Visual Baseline Collections** and open the desired collection.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/vt-collection.png" alt="Open Visual Baseline Collection" width="700"/>

2. Click on any images you want to set ignored zone for.
<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/collection-list.png" alt="Open Visual Baseline Collection" width="700"/>

3. Click **Configure Ignored Zones.** The button is then highlighted in purple, which indicates the edit mode.
4. Draw (in rectangles) to specify the area you want to ignore. The ignored zones are **highlighted in purple**. You can draw up to 20 ignored zones (i.e. 20 rectangles). If you want to apply an ignored zone to all baseline images, see: [Apply an ignored zone to all baseline images](/katalon-platform/analyze/analytics/visual-testing/use-testops-visual-testing#task-8096).

5. Click **Save**. You have temporarily saved the ignored zones on this baseline image.

    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/draw-ignored-zone.mov" type="video/mp4" />
    </video>

6. This update is currently in a draft state (e.g., Version 19 (Draft)). To **permanently** save the ignored zones under a new version, click **Save Version** at the top right corner.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/save-version.png" alt="Save changes" width="700"/>

#### Result
The baseline image now contains the defined ignored zones. During visual comparisons, these zones will be excluded, allowing for more accurate test results by ignoring dynamic or irrelevant content.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/saved-ignored-zone.png" alt="Saved ignored zone" width="700"/>

This configuration is now saved under a new version, for example, Version 19 (Latest Version):
<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/newest-version.png" alt="Newest collection" width="700"/>


### Apply an ignored zone to all baseline images

Manually adding the same ignored zone to multiple baseline images can be time-consuming, especially in large collections. With TestOps Visual Testing, you can apply an ignored zone across all baseline images.


:::caution Note
The Apply to all feature only works if all baseline images in the collection have the **same resolution** (e.g., 400×500). Zones cannot be applied across images of different sizes.
:::

To apply an ignored zone to all baseline images in a collection:

1. In your project’s UI, navigate to **Assets > Visual Baseline Collections** and open the desired collection.

<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/vt-collection.png" alt="Open Visual Baseline Collection" width="700"/>

2. Click on any images you want to set ignored zone for.
<img src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/collection-list.png" alt="Open Visual Baseline Collection" width="700"/>

3. Click **Configure Ignored Zones.** The button is then highlighted in purple, which indicates the edit mode.
4. Draw (in rectangles) to specify the area you want to ignore. These ignored zones will appear in **purple**. You can create up to 20 ignored zones per image.

    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/draw-ignored-zone1.mov" type="video/mp4" />
    </video>

5. **Click on the drawn zone**, then click the checkmark icon to confirm that you want to apply this zone to all baseline images in the collection.

6. An Acknowledge popup appears. Click **Acknowledge** to confirm.
The ignored zone now turns **green**, indicating that it has been applied to all baseline images in the collection.

7. Click **Save**. You have temporarily saved the ignored zones on this baseline image.

    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/save-acknowledge.mov" type="video/mp4" />
    </video>

8. This update is currently in a draft state (e.g., Version 19 (Draft)). To **permanently** save the ignored zones under a new version, click **Save Version** at the top right corner.

### Delete ignored zones

You can delete an ignored zone from a **single baseline image** or from **all baseline images** in the baseline collection.

- **Purple zones** indicate ignored zones applied to a **single** baseline image.
- **Green zones** indicate ignored zones applied to **all** baseline images in the collection.

1. Click **Configure Ignored Zones**. The button will be highlighted in purple, indicating that you are in edit mode.
    
2. **Click on the drawn zone**, then click the **Delete (trash can)** icon to remove it.
    - If the ignored zone is green (indicating it's applied to all images with the same resolution), a **Delete All Ignored Zones** confirmation dialog appears. Click **Delete** to confirm.
        
3. Click **Save** to temporarily save the configuration.
4. This change is currently in a draft state (e.g., Version 19 (Draft)). To **permanently** save the ignored zones under a new version, click **Save Version** at the top right corner.

    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/delete-zone.mov" type="video/mp4" />
    </video>

### Hide or unhide ignored zones when comparing checkpoint

When comparing the checkpoint image with the baseline image, you have the option to show or hide **Ignored Zones**  in the comparison interface.

<video width="600" controls>
<source src="https://tw-cdn.katalon.com/katalon-platform/visual-testing/hide-ignored-zone.mov" type="video/mp4" />
</video>

  </TabItem>
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>

## Legacy Version

### <a id="task-1507" class="anchor_top_offset"/>Configure a baseline image

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">You can set up a baseline image to compare it with the screenshot of the next Test Run. Follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Select a screenshot to see the details.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8e883e50-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-screenshot-page.png")} alt="visual checkpoint passed status" /></div></li><li className="li step stepexpand"><span className="ph cmd">Select <span className="ph uicontrol">Mark as Passed</span> at the top right corner of a screenshot, then close the screenshot.</span><div className="itemgroup stepresult"><p className="p">An <em className="ph i">Unsaved</em> label now appears on the <span className="ph uicontrol">Results</span> page.</p><p className="p"><img className="image" src={useBaseUrl("/8e86dec0-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-visual-test-run-results-page-with-unsaved-label.png")} alt="unsaved label on results page" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save to baseline</span>.</span><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">If you run a Test Suite for the first time and the Test Suite has passed, the screenshots are automatically marked as <span className="ph uicontrol">Passed</span> and there is no <span className="ph uicontrol">Save to baseline</span> button. You can open a screenshot and click <span className="ph uicontrol">Failed</span>, then switch back to <span className="ph uicontrol">Passed</span> so that the <span className="ph uicontrol">Save to baseline</span> button appears.</p></li></ul></div></div></li></ol> 

### <a id="task-1669" class="anchor_top_offset"/>Unresolved images

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">   <p className="p">If you run the Test Suite again and the new screenshots of this test execution are different from the baseline images, the status of this Visual Test Run is then marked as <span className="ph uicontrol">Unresolved</span>. To resolve these images, follow these steps:</p> </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Click on the ID of the unresolved Visual Test Run.</span></li><li className="li step stepexpand"><span className="ph cmd">Select the unresolved checkpoint.</span><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-july-visual-testing/kt-visual-testing-pixel-ui-may2022.png")} alt="mismatch image comparison method box" /><br /><br /></div><div className="itemgroup stepresult">       <p className="p">You see a drop-down list in the <span className="ph uicontrol">Comparison Method</span> section. The three options include: <span className="ph uicontrol">Pixel</span>, <span className="ph uicontrol">Layout</span>, <span className="ph uicontrol">Text Content</span>. For detailed information of each comparison method, see: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview#id_3">TestOps Visual Testing</a>.</p>     </div></li><li className="li step stepexpand"><span className="ph cmd">Select one of the three options to start comparing the new screenshot (on the right) with the baseline image (on the left).</span><div className="itemgroup info">       <div className="note note note_note"><span className="note__title">Note:</span>          <ul className="ul"><li className="li"><span className="ph uicontrol">Comparison Method</span> is enabled only if the status of the screenshot is <span className="ph uicontrol">mismatched</span>.</li></ul>       </div>     </div><div className="itemgroup info">       <ul className="ul"><li className="li">If you select <span className="ph uicontrol">Pixel</span>, check the <span className="ph uicontrol">Diffs</span> between two images (the differences are highlighted in red). See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview#id_4">Pixel-based comparison</a>.</li><li className="li">If you select <span className="ph uicontrol">Layout</span>, check the <span className="ph uicontrol">Identical</span>, <span className="ph uicontrol">Distinguishable</span> and <span className="ph uicontrol">Missing/New</span> boxes to see the differences highlighted in green/red/pink color respectively. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview#id_5">Layout-based comparison</a>.</li><li className="li">If you select <span className="ph uicontrol">Text Content</span>, check the <span className="ph uicontrol">Identical</span>, <span className="ph uicontrol">Shifted</span> and <span className="ph uicontrol">Missing/New</span> boxes to see the differences highlighted in green/blue/pink color respectively. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview#id_6">Content-based comparison</a>.</li></ul>     </div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Mark as Passed</span> or <span className="ph uicontrol">Mark as Failed</span> to resolve.</span><div className="itemgroup info">       <div className="note note note_note"><span className="note__title">Note:</span>          <ul className="ul"><li className="li">The <span className="ph uicontrol">Unsaved</span> label appears whenever you change the status (<span className="ph uicontrol">Passed</span> or <span className="ph uicontrol">Failed</span>) of a screenshot. If you click <span className="ph uicontrol">Save to baseline</span>, the new <span className="ph uicontrol">Passed</span> screenshot replace the older baseline image. Katalon TestOps then compares between the new baseline image and screenshots of the next Visual Test Run.</li></ul>       </div>     </div></li></ol> 

### <a id="concept-6436" class="anchor_top_offset"/>Ignored zones

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Specifying ignored zones is especially useful when testing a website with some dynamic and changing content (such as pop-up ads on specific areas). Visual testing can ignore such content while comparing captured images with the baseline one. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In TestOps Visual Testing, you can configure an ignore zone in a baseline image and apply this ignored zone to all baseline images in the baseline collection. You can also delete the ignored zone(s) in all baseline images.</p> 

#### <a id="task-44" class="anchor_top_offset"/>Add an ignored zone to a baseline image

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"> To configure an ignored zone, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://testops.katalon.io" target="_blank">Katalon TestOps</a> and go to your project.</span></li><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Visual Testing</span> &gt; <span className="ph uicontrol">Visual Baseline Collections</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">Select the <span className="ph uicontrol">Baseline Collection ID</span> you want to check.</span><div className="itemgroup info">The list of baseline images appears.<p className="p">         <svg xmlns="http://www.w3.org/2000/svg" height={371} id="svgcontent" overflow="visible" viewBox="0 0 768 371" width={768} x={768} y={371} className="anchor_top_offset"><g style={{pointerEvents: 'all'}}><title style={{pointerEvents: 'inherit'}}>Layer 1              </title><image height={371} id="svg_99c42c0f-a3e4-481b-a171-133fe2c1e85c" width={768} actuate="onLoad" href="https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-july-visual-testing/kt-baseline-collection-id-ui-jun22.png" show="embed" type="simple" className="anchor_top_offset" /><rect fill="#000000" fillOpacity={0} height={22} id="svg_1" rx={5} ry={5} stroke="#6bb545" strokeOpacity={1} strokeWidth={4} width="22.999999796190565" x="138.50000020380944" y="213.5" className="anchor_top_offset" /></g></svg>       </p></div></li><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">Edit image</span> icon of the baseline image you want to configure (e.g., the baseline image <span className="ph uicontrol">image10</span>).</span><div className="itemgroup stepresult">The page displays as below.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-july-visual-testing/kt-edit-baseline-image10-ui-jun22.png")} alt="configure ignored zone in image10" /><br /><br /></div></li><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">Configure Ignored Zones</span> button.</span><div className="itemgroup info">The button is then highlighted in blue, which indicates the edit mode.</div><div className="itemgroup stepresult"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-july-visual-testing/kt-configure-ignored-zones-button-in-blue-ui-jun22.png")} alt="configure ignored zones button highlighted" /><br /><br /></div></li><li className="li step stepexpand"><span className="ph cmd">Draw (in rectangles) to specify the area you want to ignore.</span><div className="itemgroup info">The ignored zones are highlighted in purple. You can draw up to 20 ignored zones (i.e. 20 rectangles). <div className="note note note_note"><span className="note__title">Note:</span>          <ul className="ul"><li className="li">             <p className="p">If you want to apply an ignored zone to all baseline images, see: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/use-testops-visual-testing#task-8096">Apply an ignored zone to all baseline images</a>.</p>           </li></ul>       </div></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save</span>.</span><div className="itemgroup info">You have temporarily saved the ignored zones on this baseline image.</div><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-july-visual-testing/kt-ignored-zone-in-purple-ui-jun22.png")} alt="save baseline image10" /><br /><br />       <div className="note note note_note"><span className="note__title">Note:</span>          <ul className="ul"><li className="li">You have not permanently saved the configuration of ignored zones at this stage. </li></ul>       </div>     </div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save Changes</span> on the top right corner to permanently save the ignored zones you have configured.</span><div className="itemgroup stepresult"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-july-visual-testing/kt-save-changes-button-enabled-ui-jun22.png")} alt="save changes button for baseline collection" /><br /><br /></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">The baseline image has now had ignored zones. Visual testing then ignores these zones when comparing captured images with this baseline image. <p className="p">When comparing the checkpoint image with the baseline image, you can show or hide the ignored zones by ticking/un-ticking the <span className="ph uicontrol">Ignored Zones</span> checkbox.</p><svg xmlns="http://www.w3.org/2000/svg" height={371} id="svg_05b31f80-0f75-408e-90b3-adc5260a28c4" overflow="visible" viewBox="0 0 776 371" width={776} x={776} y={371} className="anchor_top_offset"><g style={{pointerEvents: 'all'}}><title style={{pointerEvents: 'inherit'}}>Layer 1        </title><image height={371} id="svg_620afdad-4cdc-489d-8e44-4bcca3900d72" width={776} actuate="onLoad" href="https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-july-visual-testing/kt-visual-testing-ignored-zones-ticked-ui-jun22.png" show="embed" type="simple" className="anchor_top_offset" /><rect fill="#000000" fillOpacity={0} height={24} id="svg_0198729a-f496-4218-8634-989f4794c43a" rx={5} ry={5} stroke="#6bb545" strokeOpacity={1} strokeWidth={4} style={{pointerEvents: 'inherit'}} width={89} x="204.83333333333326" y="41.5" className="anchor_top_offset" /></g></svg></section> 

#### <a id="task-8096" class="anchor_top_offset"/>Apply an ignored zone to all baseline images

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Adding an ignored zone to the same area in multiple baseline images could become time-consuming if there are more than one baseline image. With TestOps Visual Testing, you can apply an ignored zone to multiple baseline images in a baseline collection.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><p className="p">To apply an ignored zone to all baseline images within one baseline collection, follow these steps:</p> </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Configure an ignored zone. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/use-testops-visual-testing#task-44">Add an ignored zone to a baseline image</a>.</span><div className="itemgroup stepresult">The ignored zone is displayed in purple.</div></li><li className="li step stepexpand"><span className="ph cmd">Click on the ignored zone, then select the <span className="ph uicontrol">Apply the zone to all images</span> icon.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8e82e720-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-apply-zone-to-all-icon.png")} alt="apply ignored zone to all images icon" /></div><div className="itemgroup stepresult">You then see the <span className="ph uicontrol">Acknowledgement</span> pop-up box.<img className="image" src={useBaseUrl("/8e81d5b0-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-acknowledgement-box.png")} alt="ignored-zone-acknowledgement-popup" /></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Acknowledge</span>.</span><div className="itemgroup stepresult"> The ignored zone is now displayed in yellow because it has been applied to all other baseline images in the baseline collection.<img className="image" src={useBaseUrl("/8e80c440-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-ignored-zone-applied-to-all.png")} alt="ignored zone applied to all images" /></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save</span> to temporarily save the configuration.</span></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save Changes</span> on the top right corner to permanently save the configuration.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have applied an ignored zone to all baseline images within the selected baseline collection.</section> 

### <a id="task-5282" class="anchor_top_offset"/>Delete ignored zones

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">You can delete an ignored zone in one baseline image and/or all baseline images in the baseline collection.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">An ignored zone applied to one baseline image only is displayed in purple. To delete it, click on the ignored zone and select the <span className="ph uicontrol">Delete ignored zone</span> icon. <p className="p">An ignored zone applied to all baseline images is displayed in yellow. To delete it, follow these steps:</p>  </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Click on the ignored zone and select the <span className="ph uicontrol">Delete ignored zone</span> icon.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8e84e2f0-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-delete-ignored-zone-icon.png")} alt="delete ignored zone icon" /></div><div className="itemgroup stepresult">The <span className="ph uicontrol">Delete all ignored zones</span> box pops up.<img className="image" src={useBaseUrl("/8e83d180-22b2-11ed-9930-0242fe3e4a3f/kte-jul2022-delete-all-ignored-zone-popup.png")} alt="delete all ignored zones popup box" /></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Delete all zones</span> to confirm your action.</span></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save</span> to temporarily save the configuration.</span></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save Changes</span> to permanently save this configuration. </span><div className="itemgroup stepresult">The ignored zone is now deleted in all baseline images of the baseline collection.</div></li></ol> 

  </TabItem>
</Tabs>