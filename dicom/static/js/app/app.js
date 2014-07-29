var dicom = angular.module('dicom', ['ngRoute']);

dicom.config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    }
);

dicom.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'static/views/dummy.html',
            controller: 'DummyCtrl'
        })
        .otherwise({
            reidrectTo: '/'
        })
})