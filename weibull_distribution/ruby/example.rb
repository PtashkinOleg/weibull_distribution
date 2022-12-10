require_relative 'weibull_distribution'
require "csv"

class Example < Rubystats::WeibullDistribution
  include Rubystats::NumericalConstants

    scale = rand(1.0..5.0)
    shape = rand(1.0..5.0)
    wbd = Rubystats::WeibullDistribution.new(scale,shape)

  path = '/test.csv'
  CSV.open("test.csv", "wb") do |csv|
    csv << ['scale','shape','PDF','CDF']
    csv << [scale,shape,wbd.pdf(1),wbd.cdf(1)]

  end
end
