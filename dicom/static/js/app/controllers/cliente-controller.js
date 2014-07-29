dicom.controller('ClienteController', function ($scope, $routeParams, $location, ClienteService) {

    ClienteService.list().then(function(data) {
        $scope.clientes = data;
    });
});