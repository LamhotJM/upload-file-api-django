CREATE TABLE comments (
    commentid int,
    userid character varying(100),
    loanid character varying(100),
    comment varchar,
    file_upload varchar,
    context_id int,
    context_scope varchar,
    status int,
    createdby character varying(60) NOT NULL,
    createddate timestamp without time zone,
    createdfrom character varying(25) NOT NULL,
    modifiedby character varying(60),
    modifieddate timestamp without time zone,
    modifiedfrom character varying(25),
     PRIMARY KEY (commentid )
    )


INSERT INTO public.comments(
            commentid, userid, loanid, comment, file_upload, context_id,
            context_scope, status, createdby, createddate, createdfrom, modifiedby,
            modifieddate, modifiedfrom)
    VALUES (1, 1, 1, 'comment lorem ipsum', 'file upload', 1,
            'contex lorem ipsum', 1, 'createdby Jhon Doe', '2038-01-19 03:14:07',
            'Created From','modifiedby Jhon Doe', '2038-01-19 03:14:07', 'Modifield From');
