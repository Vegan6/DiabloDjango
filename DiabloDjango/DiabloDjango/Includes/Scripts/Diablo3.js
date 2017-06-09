/// Menu
(function () {
	
    var collapseMenuItem = function (obj) {
        var div = obj.target, child;

        while (!div.className.includes("menuItem")) {
            div = div.parentElement;
        }

        child = div.getElementsByTagName("div")[0];

        console.log(child.style.height);

        if (child.style.height !== "0px") {
            child.style.height = "0px";
        } else {
            child.style.height = child.attributes["data-height"];
        }
	    
	};

	var events = function () {
	    var items = document.getElementsByClassName("menuItem");

	    console.log(items);

	    for (var i = 0; i < items.length; i += 1) {
	        var item = items[i].getElementsByTagName("div")[0];

	        if (item) {
	            item.attributes['data-height'] = item.offsetHeight + "px";

	            //item.addEventListener("click", collapseMenuItem);

	            item.parentElement.addEventListener("click", collapseMenuItem);
	            console.log(item.attributes['data-height']);

	            console.log(item.parentElement);
	        }
	        
	    }


	    //document.getElementsByClassName("menuItem").addEventListener("click", collapseMenuItem);
	}

	this.onload = function () {
	    events();
	}
    
}());

