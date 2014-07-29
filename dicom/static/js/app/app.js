var dicom = angular.module('dicom', ['ngRoute', 'ngCookies']);

dicom.config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    }
);

dicom.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})

dicom.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'static/views/clientes.html',
            controller: 'ClienteController'
        })
        .otherwise({
            reidrectTo: '/'
        })
})