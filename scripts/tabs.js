// tabs.js

function showTab(tab) {
	
	// Reset all tabs and their contents
	tabs.forEach(function(currentTab) {
		currentTab.style.backgroundColor = defaultTabFillColor;
	});
	
	tabContents.forEach(function(currentTabContent) {
		
		currentTabContent.style.display = 'none';
		
	});
	

	
	const correspondingContent = tabs.indexOf(tab);
	
	// Change the tab color and its corresponding content
	tab.style.backgroundColor = activeTabFillColor;
	tabContents[correspondingContent].style.display = 'block'; 
	
}


const activeTabFillColor = '#ffff80';
const defaultTabFillColor = '#ffffb3';

const tabs = Array.from(document.querySelectorAll('.tab'));
const tabContents = document.querySelectorAll('.tab-content')

// Set default tab
tabs[0].style.backgroundColor = activeTabFillColor;
tabContents[0].style.display   = 'block';

tabs.forEach(function(currentTab) {
	
	currentTab.addEventListener('click', function() {
		showTab(currentTab);
	});

});