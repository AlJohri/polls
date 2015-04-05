'use strict';

/**
 * @ngdoc function
 * @name pollsApp.controller:RCPCtrl
 * @description
 * # RCPCtrl
 * Controller of the pollsApp
 */
angular.module('pollsApp')
  .controller('QuinnipiacCtrl', function ($scope, Ref, $firebaseArray, $timeout, $http, $q) {

    $scope.quinnipiac = $firebaseArray(Ref.child('quinnipiac'));
    $scope.quinnipiac.$loaded().catch(alert);

    function alert(msg) {
      $scope.err = msg;
      $timeout(function() {
        $scope.err = null;
      }, 5000);
    }

    $scope.refreshQuinnipiac = function() {
      $http.get("http://todayspolls.herokuapp.com/quinnipiac")
    }

  });
