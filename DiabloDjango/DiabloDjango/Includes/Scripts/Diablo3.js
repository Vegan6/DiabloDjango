/// Menu
(function () {
	
    var collapseMenuItem = function (obj) {
        if (obj.target.nextElementSibling.className !== "menuItem") {
            var item = obj.target.nextElementSibling;
            
            if (item.style.display == "none") {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        }
	    
	};

	var events = function () {
	    //var items = document.getElementsByClassName("menuItem");

	    //for (var i = 0; i < items.length; i += 1) {
	    //    items[i].addEventListener("click", collapseMenuItem);
	    //}

	    document.getElementsByClassName("heroListItem")[0].addEventListener("click", collapseMenuItem);
	}

	this.onload = function () {
	    events();
	}
    
}());

