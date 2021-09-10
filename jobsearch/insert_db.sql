USE jobmonitor;

INSERT INTO public.jobsearch_status (advanced)
VALUES
('CV sent'),
('To apply'),
('Positive answer'),
('Negative answer'),
('Job interview');


INSERT INTO public.jobsearch_typeofcontract (type)
VALUES
('Permanent'),
('Fixed-term'),
('Working student'),
('Internship'),
('Freelance'),
('Casual'),
('others');


INSERT INTO public.jobsearch_styleofcontract (style)
VALUES
('Full time'),
('Part time'),
('Casual'),
('others');


Truncate TABLE public.jobsearch_status restart identity cascade;

ALTER TABLE public.jobsearch_joboffer ADD column company_name VARCHAR(150) Null;


INSERT INTO public.jobsearch_status (advanced)
VALUES
('CV envoyé'),
('A Postuler'),
('Réponse positive'),
('Réponse Négative'),
('Entretien');


INSERT INTO public.jobsearch_typeofcontract (type)
VALUES
('CDI'),
('CDD'),
('Alternance'),
('Stage'),
('Freelance'),
('Extras'),
('autres');


INSERT INTO public.jobsearch_styleofcontract (style)
VALUES
('Temps plein'),
('Mi-temps'),
('Extras'),
('autres');
