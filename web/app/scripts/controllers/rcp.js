'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:RCPCtrl
 * @description
 * # RCPCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('RCPCtrl', function ($scope, Ref, $firebaseArray, $timeout, $http, $q) {

    $scope.rcp = $firebaseArray(Ref.child('rcp'));
    $scope.rcp.$loaded().catch(alert);

    function alert(msg) {
      $scope.err = msg;
      $timeout(function() {
        $scope.err = null;
      }, 5000);
    }

    $scope.refreshRCP = function() {
      $http.get("http://todayspolls.herokuapp.com/rcp")
    }

  });
