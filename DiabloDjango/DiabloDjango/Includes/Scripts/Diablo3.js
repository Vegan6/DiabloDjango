/// Menu
(function () {
	var layout = function () {
	    
        
	};

	var collapseMenuItem = function (obj) {
	    var item = obj.target.nextElementSibling;
        
	    if (item.style.display == "none") {
	        item.style.display = "block";
	    } else {
	        item.style.display = "none";
	    }
	    
	};

	var events = function () {
	    //var items = document.getElementsByClassName("menuItem");

	    //for (var i = 0; i < items.length; i += 1) {
	    //    items[i].addEventListener("click", collapseMenuItem);
	    //}

	    document.getElementsByClassName("heroListItem")[0].addEventListener("click", collapseMenuItem);
	}

	//#region Handles the event when the window loads
	this.onload = function () {
	    events();
	}

	//#endregion

}());

