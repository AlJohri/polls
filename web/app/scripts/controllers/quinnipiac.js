'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:QuinnipiacCtrl
 * @description
 * # QuinnipiacCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('QuinnipiacCtrl', function ($scope) {
  	$scope.status = $scope.$parent.status;
    $scope.quinnipiac = $scope.$parent.quinnipiac;
    $scope.refreshQuinnipiac = $scope.$parent.refreshQuinnipiac;
  });
