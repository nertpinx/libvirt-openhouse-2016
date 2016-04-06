
var app = angular.module('lvWebSandbox', []);

app.controller('lwsCtrl', function($scope, $http) {
    $scope.domains = {};
    $scope.buttons = [
	{ 'name' : 'Start', 'action' : 'create' },
        { 'name' : 'Destroy', 'action' : 'destroy' },
	{ 'name' : 'Get Address', 'action' : 'interfaceAddresses' },
    ];

    var handleResult = function($scope, data) {
        if ("error" in data)
            $scope.errorText = data.error;
        else
            $scope.errorText = "";

        if ("update" in data)
            $.extend(true, $scope.domains, data.update);
        else if ("domains" in data)
            $scope.domains = data.domains;
    }

    $scope.doAction = function(action, name) {
        var url = "/do/" + action

        if (name)
            url = url + "?name=" + name

        $http.get(url).then(function(r) {
            var data = angular.fromJson(r.data);
            console.log("Got data: " + angular.toJson(data));
            handleResult($scope, data);
        }, function(r) {
            $scope.errorText = "Error " + r.status + ": " + r.statusText;
        });
    }

    $http.get("/list").then(function(r) {
        var data = angular.fromJson(r.data);
        console.log("Got data: " + angular.toJson(data));
        $scope.domains = data.domains;
    }, function(r) {
        $scope.errorText = "Error " + r.status + ": " + r.statusText;
    });
});
