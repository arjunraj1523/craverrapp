	    
	var app = angular.module('myApp', []);
	 app.controller('customersCtrl', function($scope, $http) {
	    $(document).ready(function(){
	    update();

	});
/*
	function callSetTimeout(){
	    setTimeout(function(){
	        update();
	        callSetTimeout();
	    },0);
	}
*/
	 function update(){
	    $http.get("http://localhost/craverApp/TemplatesForWebsite/main_website/php/getUrl.php")
	          	.success(function (response) {$scope.names= response.records;});
	                  }
	 });
