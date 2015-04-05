'use strict';
/**
 * @ngdoc overview
 * @name pollsApp:routes
 * @description
 * # routes.js
 *
 * Configure routes for use with Angular, and apply authentication security
 */
angular.module('pollsApp')

  .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
      })

      .when('/rcp', {
        templateUrl: 'views/rcp.html',
        controller: 'RCPCtrl'
      })

      .when('/hp', {
        templateUrl: 'views/hp.html',
        controller: 'HPCtrl'
      })
      .otherwise({redirectTo: '/'});
  }]);