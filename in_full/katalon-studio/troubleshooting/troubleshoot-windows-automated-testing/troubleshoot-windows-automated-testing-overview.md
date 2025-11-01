---
title: Troubleshoot Windows automated testing overview
---

import DocCardList from '@theme/DocCardList'; 
import {useCurrentSidebarCategory} from '@docusaurus/theme-common'; 

export default function TroubleshootingIndex() {

  const category = useCurrentSidebarCategory();

  // Skip the first item (index 0)
  const items = category.items.slice(1);

  return <DocCardList items={items} />;
}