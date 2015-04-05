'use strict';

angular.module('pollsApp')
  .filter('reverse', function() {
    return function(items) {
      return angular.isArray(items)? items.slice().reverse() : [];
    };
  });

angular.module('pollsApp')
	.filter('join', function() {
		return function(list, token) {
	    return (list||[]).join(token);
		};
	});

angular.module('pollsApp')
	.filter('pluck', function() {
	    return function(objects, property) {
	    	return _.pluck(objects, property);
	    };
	});

angular.module('pollsApp')
	.filter('pluck2', function() {
	    return function(objects, property1, property2) {
	    	return _.chain(objects)
	    		.map(function(obj) { return _.pick(obj, [property1, property2]); })
	    		.map(function(obj) { return obj[property1] + ": " + obj[property2] + "%"; })
	    		.flatten()
	    		.value();
	    	// return _.pluck(objects, property1);
	    };
	});