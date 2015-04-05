'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:HeaderCtrl
 * @description
 * # HeaderCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('HeaderCtrl', function ($scope, $location) {
  	$scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
});