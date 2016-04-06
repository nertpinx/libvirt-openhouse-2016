
var app = angular.module('lvWebSandbox', []);

app.controller('lwsCtrl', function($scope, $http) {
    $scope.domains = [];

    $http.get("/list").then(function(r) {
        var data = angular.fromJson(r.data);
	console.log("Got data: " + angular.toJson(data));
	$scope.domains = data.domains;
    }, function(r) {
	$scope.errorText = "Error " + r.status + ": " + r.statusText;
    });
});
