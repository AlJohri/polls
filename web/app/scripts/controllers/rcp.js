'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:RCPCtrl
 * @description
 * # RCPCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('RCPCtrl', function ($scope) {
  	$scope.status = $scope.$parent.status;
    $scope.rcp = $scope.$parent.rcp;
    $scope.refreshRCP = $scope.$parent.refreshRCP;
  });
