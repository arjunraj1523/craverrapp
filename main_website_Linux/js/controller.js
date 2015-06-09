var craverrappConfig = function($routeProvider) {
$routeProvider
.when('/', {
controller: '',
templateUrl: '../cgi/test.html'
})
;
};
var CraverrApp = angular.module('CraverrApp', []).
config(craverrappConfig);