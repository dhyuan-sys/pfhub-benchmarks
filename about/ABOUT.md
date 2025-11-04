# About PFHub

#### Primary PFHub Goals

1. Provide a set of benchmark problems to compare and contrast codes for
   solving phase field equations.

2. Provide quality assurance for phase field codes based on
   performance and accuracy.

3. Increase the adoption of phase field methods in engineering and
   academic applications with the development of practical
   documentation.

4. Foster an engaged and integrated phase field community.

#### Details and Mentions

- Olle Heinonen wrote a philosophical introduction to the PFHub
  benchmarking effort, available as an [extended essay](./BENCHMARKS_ESSAY.md).
- [Andrea Jokisaari][aj], [Peter Voorhees][pv], [Jon Guyer][jg], [Jim Warren][jw] and [Olle Heinonen][oh]
  published a peer-reviewed journal article in
  *Computational Materials Science* entitled ["Benchmark problems for numerical
  implementations of phase field models"](http://dx.doi.org/10.1016/j.commatsci.2016.09.022).
- CHiMaD News posted an overview of the article entitled
  ["Benchmark Problems for Phase Field Methods"](http://chimad.northwestern.edu/news-events/articles/2016/PhaseField_BenchMark.html).
- Aashutosh Mistry wrote an overview of the presentation delivered by
  [Jon Guyer][jg] at MRS 2017 entitled ["Benchmarking Problems for Phase Field Codes"](
  http://materials.typepad.com/mrs_meeting_scene/2017/11/tc05-uncertainty-quantification-in-multiscale-materials-simulation-1.html).

#### Get Involved

We are an inclusive and expanding community and welcome new
participants.  All those interested in phase field modeling are
welcome to participate in a variety of different ways. See the
[involvement guide](./INVOLVEMENT.md) for more details
about how you can get involved with the community.

#### Community

Please see the [community page](./COMMUNITY.md) for
details of individuals involved in this project and their
affiliations.

#### Code of Conduct

We have a code of conduct and enforce it in our online interactions
and codebase. Please see the [code of conduct page](./CODE_OF_CONDUCT.md) for further details.

#### Suggested Phase Field Codes

The goal of this site is to not only generate benchmarks, but to also
evaluate codes that solve phase field problems. We have a list of
[suggested codes](./SUGGESTED_CODES.md) that have been used to
solve some of the benchmark problems.

#### FAQ

##### Which code should I use to solve my phase field problem?

The right code for you depends on your familiarity with phase field
methods and relevant software, hardware available and complexity of
the phase field problem under consideration. We have a [list of phase
field codes](./SUGGESTED_CODES.md) and also a [list of benchmark
results]({{ site.baseurl }}/simulations/#simulations) that might help
you evaluate which code might work best for you. Our objective is that
the benchmarks will support users of the site in evaluating the
suitability of codes for particular classes of phase field problems,
but the user is the final arbiter in this process.

##### I don't like one of the benchmark problems. Can I help fix it?

Yes. Your feedback on the benchmark problems is highly valued. The
benchmarks are a moving target that you can contribute to. If you
would like to propose a change or improvement then please raise it via
[chat]({{ site.links.chat }}) or as an [issue]({{ site.links.github
}}/issues/new). The community will discuss the change and act on it if
we can reach a consensus

##### Who is PFHub Intended For?

The Phase Field Community Hub is relevant to the diverse spectrum of
phase-field community members, from newcomers to established experts in the
theory, practice, and implementation of mesoscale models. The following
"user stories" roughly sketch out how we intend this website to be of use
to a few representative visitors.

(about:novice)=
###### Novice Users

A novice (<i>e.g.</i>, graduate student) may have been directed to choose a
code and start modeling by an advisor or teacher, with no knowledge of
phase field methods or our jargon. This user will not know exactly what
they're looking for. While basic education is beyond the scope of PFHub,
we can help address the following questions.

- <b>What is "phase-field"?</b> To help this new user come up to speed, the
  website provides a set of [video lectures]({{ site.baseurl
  }}/wiki/voorhees-lectures/) by Prof. [Peter Voorhees][pv] introducing
  the fundamental theory of phase-field methods.
- <b>How do I do it?</b> To help this new user launching simulations, the
  website provides a list of [suggested codes](./SUGGESTED_CODES.md),
  briefly summarizing programming language, parallelization models,
  numerical methods, license, up-front and ongoing costs, and major
  dependencies.

(about:intermediate)=
###### Advanced Users

An advanced user (<i>e.g.</i>, early-career researcher) with experience in
phase-field modeling might change positions or focus, and take a moment to
survey the software landscape. This user will have some idea what they're
looking for, or specifically guarding against. Focus may be suitability to
a specific task, or flexibility to address a wide variety of tasks. The
researcher might be wondering...

- <b>Are my results in line?</b> To help the experienced
  user compare their performance against other users of the same code, the
  website provides the following:
    - A simple process for submitting simulation results with rapid
      feedback: new work appears in the graphs and tables on a
      test website, allowing iteration if the results are out of line.
    - Access to the source code for prior submissions.
- <b>Is something better out there?</b> To help the experienced user drill
  down on options, the website provides the following:
    - A list of [suggested codes](./SUGGESTED_CODES.md).
    - A dashboard showing how many results have been submitted using each
      code for each benchmark problem.
    - Visual summaries of relative performance of these codes on each
      benchmark problem.

(about:expert)=
###### Expert Users

An expert user (<i>e.g.</i>, software developer) experienced with
phase-field models and numerical methods will be interested in upgrading
their code, making it easier to use, more powerful, or able to run on
evolving hardware and software platforms. The developer might be
wondering...

- <b>Is my code competitive?</b> To help the developer compare apples to
  apples, the website provides the following:
    - List of available simulation results, with visualizations and ability
      to filter by code, platform, and author (fellow dev or user).
    - A Benchmark Problem using the method of manufactured solutions to
      help verify the discretization and numerical methods.
    - A responsive process for uploading simulation results when new
      benchmarks come out.

###### Advisors (<i>e.g.</i>, faculty)

A faculty adviser who is continually having new researchers join their
research group that are unfamiliar with the phase field method will be
interested in having a collection of example problems with known,
recorded solutions that their students can implement while learning.

- <b>Are New Researchers Solving Problems Correctly?</b> To best instruct
  new researchers, the website should provide:
    - Problems with all parameters, initial conditions, and boundary
      conditions defined.
    - Well established solutions using a range of different solution
      methods that new researchers can use for comparison.
    - Metrics from other codes showing computation times that new
      researchers can use to evaluate the efficiency of their
      solution.
- <b>Are They Learning A Range of Phase Field Problems?</b> To provide
  new researchers with a breadth of knowledge, rather than in just one
  area, the website should provide
    - Problems covering a range of different materials phenomena.
    - Problems with increasing complexity.
    - Problems with unique aspects such as coupled mechanics or
      anisotropic surface energy.

[aj]: {{ site.baseurl }}/community/#andrea-jokisaari
[jg]: {{ site.baseurl }}/community/#jon-guyer
[oh]: {{ site.baseurl }}/community/#olle-heinonen
[pv]: {{ site.baseurl }}/community/#peter-voorhees
[jw]: {{ site.baseurl }}/community/#james-warren
