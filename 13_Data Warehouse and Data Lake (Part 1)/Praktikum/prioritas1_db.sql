failed to get console mode for stdout: The handle is invalid.
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: citus; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS citus WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION citus; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citus IS 'Citus distributed database';


--
-- Name: citus_columnar; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS citus_columnar WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION citus_columnar; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citus_columnar IS 'Citus Columnar extension';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    post_id integer,
    user_id integer,
    content character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.comments OWNER TO postgres;

--
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.comments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.comments_id_seq OWNER TO postgres;

--
-- Name: comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.comments_id_seq OWNED BY public.comments.id;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    user_id integer,
    category_id integer,
    title character varying NOT NULL,
    content text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.posts_id_seq OWNER TO postgres;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: comments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments ALTER COLUMN id SET DEFAULT nextval('public.comments_id_seq'::regclass);


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id, name, created_at, updated_at) FROM stdin;
1	category1	2024-12-06 11:57:08.929051	2024-04-22 02:03:19.16282
2	category2	2024-04-21 05:02:25.053328	2024-05-05 07:07:52.164352
3	category3	2024-07-10 10:17:37.245713	2024-11-26 05:16:21.920584
4	category4	2024-10-23 05:07:59.092751	2025-01-06 20:41:59.582497
5	category5	2025-03-23 21:28:28.762485	2024-09-28 16:54:00.939369
6	category6	2024-08-05 02:45:43.095631	2024-12-29 19:14:12.714223
7	category7	2024-05-30 12:54:49.588459	2024-05-05 04:32:53.499956
8	category8	2024-11-03 18:46:12.493463	2024-11-05 10:49:35.144851
9	category9	2024-07-10 20:41:00.760206	2024-09-10 20:36:05.434887
10	category10	2025-01-13 02:13:51.129491	2024-12-31 23:50:49.626481
\.


--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.comments (id, post_id, user_id, content, created_at, updated_at) FROM stdin;
1	9	3	comments content 1	2024-12-31 05:15:52.490991	2024-08-10 23:39:28.240083
2	2	6	comments content 2	2024-03-30 23:30:50.28792	2024-04-16 20:10:15.959711
3	4	4	comments content 3	2024-11-09 07:11:33.534309	2024-04-27 04:44:16.199915
4	8	6	comments content 4	2024-10-24 16:35:38.201996	2024-12-26 07:30:13.955085
5	6	4	comments content 5	2024-08-07 14:38:09.935333	2024-04-13 14:53:23.735448
6	7	8	comments content 6	2024-09-17 09:09:24.569561	2024-12-25 18:29:26.840373
7	5	3	comments content 7	2024-06-17 01:04:43.881588	2024-09-21 17:56:22.397308
8	2	2	comments content 8	2024-08-06 11:25:09.085874	2024-06-18 12:54:19.698327
9	10	10	comments content 9	2024-10-03 01:02:50.167573	2024-05-24 10:28:57.850709
10	2	8	comments content 10	2025-03-27 03:04:29.055558	2024-11-16 22:22:58.814075
\.


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.posts (id, user_id, category_id, title, content, created_at, updated_at) FROM stdin;
1	8	6	title1	this is content 1	2024-06-21 20:18:52.035374	2025-03-22 20:48:06.291006
2	3	2	title2	this is content 2	2024-07-11 10:19:06.978892	2024-06-15 06:45:12.736894
3	6	8	title3	this is content 3	2024-04-05 03:53:38.178003	2024-09-05 12:27:03.420089
4	9	1	title4	this is content 4	2025-03-21 10:01:23.942633	2025-01-10 15:05:57.82446
5	8	6	title5	this is content 5	2024-08-26 02:57:40.138217	2025-01-03 17:54:52.572253
6	7	2	title6	this is content 6	2024-08-24 15:05:41.389403	2024-10-31 00:02:30.219769
7	8	3	title7	this is content 7	2025-02-02 20:29:44.786216	2024-07-14 07:10:12.855401
8	9	2	title8	this is content 8	2025-01-16 04:56:47.825016	2024-07-24 01:34:59.29223
9	2	4	title9	this is content 9	2024-05-31 16:53:38.212587	2024-08-28 05:44:50.995907
10	9	1	title10	this is content 10	2024-11-18 04:09:31.646995	2024-12-21 07:43:22.7674
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, password, created_at, updated_at) FROM stdin;
1	user1	pass1	2024-10-08 09:17:40.460962	2024-06-20 12:44:50.06169
2	user2	pass2	2024-09-22 18:21:30.720433	2024-04-29 11:01:13.326236
3	user3	pass3	2024-08-04 00:32:54.072808	2024-07-20 20:00:43.896427
4	user4	pass4	2024-09-21 12:30:36.16314	2024-06-13 14:16:57.996375
5	user5	pass5	2024-08-10 16:51:13.797032	2025-02-17 08:24:58.309196
6	user6	pass6	2024-10-22 13:30:10.520067	2025-02-10 14:58:22.900603
7	user7	pass7	2024-06-03 22:52:32.050376	2024-09-20 17:18:37.556152
8	user8	pass8	2024-07-20 18:43:46.446064	2024-06-22 14:15:57.585946
9	user9	pass9	2024-11-08 00:26:41.202665	2024-10-24 14:36:06.541563
10	user10	pass10	2024-06-22 04:02:51.959909	2024-09-02 10:11:16.701156
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 10, true);


--
-- Name: comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.comments_id_seq', 10, true);


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_id_seq', 10, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 10, true);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: posts fk_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- Name: comments fk_post; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT fk_post FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- Name: posts fk_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: comments fk_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

