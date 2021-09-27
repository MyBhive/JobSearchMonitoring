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


INSERT INTO public.jobsearch_joboffer (title, company_name, url, date, salary, comments, category_id_id, status_id_id, style_id_id, type_id_id, user_id_id)
values ('dev python',
		'oc',
		'https://www.studi.com/fr/formation/gestion-de-projet/mba-chief-digital-officer',
		'26/09/2021',
		'33000',
		'Identifier les compétences et outils nécessaires au développement dune stratégie digitale. Concevoir et déployer une stratégie de marketing digital de A à Z. Gérer un projet digital. Conduire le changement et accompagner linnovation. Elaborer une solution technologique et maîtriser les langages de programmation associés',
		1,
		2,
		3,
		1,
		1)